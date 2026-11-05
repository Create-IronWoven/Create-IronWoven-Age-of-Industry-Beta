#!/usr/bin/env python3
"""Apply a submitted GitHub issue-form test result to TESTING_CHECKLIST.md."""
from __future__ import annotations
import base64, json, os, re, time, urllib.error, urllib.request
from pathlib import Path

API = "https://api.github.com"
TOKEN = os.environ["GITHUB_TOKEN"]
REPOSITORY = os.environ["GITHUB_REPOSITORY"]
ISSUE_NUMBER = int(os.environ["ISSUE_NUMBER"])
EVENT_PATH = os.environ["GITHUB_EVENT_PATH"]
CHECKLIST_PATH = "TESTING_CHECKLIST.md"

def api(method: str, path: str, payload: dict | None = None):
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(API + path, data=data, method=method, headers={
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28",
        "Content-Type": "application/json",
        "User-Agent": "Create-IronWoven-test-result-updater",
    })
    with urllib.request.urlopen(request, timeout=30) as response:
        raw = response.read()
        return json.loads(raw.decode("utf-8")) if raw else {}

def comment(message: str):
    api("POST", f"/repos/{REPOSITORY}/issues/{ISSUE_NUMBER}/comments", {"body": message})

def field(body: str, label: str) -> str:
    pattern = rf"(?ms)^### {re.escape(label)}\s*\n(.*?)(?=^### |\Z)"
    match = re.search(pattern, body)
    if not match:
        return ""
    value = match.group(1).strip()
    return "" if value in {"_No response_", "_No response"} else value

def clean(value: str) -> str:
    return " ".join(value.strip().split())

def md_cell(value: str) -> str:
    return clean(value).replace("|", r"\|").replace("\r", " ").replace("\n", " ")

def locate_section(lines: list[str], requested: str):
    requested = clean(requested).lstrip("#").strip()
    headings = [i for i, line in enumerate(lines)
                if line.startswith("### ") and clean(line[4:]).casefold() == requested.casefold()]
    if len(headings) != 1:
        return None, "Could not find one unique mod heading. Copy the complete heading, including version, from TESTING_CHECKLIST.md."
    start = headings[0]
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if lines[i].startswith("### ") or lines[i].startswith("## "):
            end = i
            break
    return (start, end), None

def update_checklist(mod_heading: str, action: str, result: str, tester: str, date: str, evidence: str):
    path = f"/repos/{REPOSITORY}/contents/{CHECKLIST_PATH}"
    for attempt in range(4):
        file_info = api("GET", path + "?ref=main")
        content = base64.b64decode(file_info["content"]).decode("utf-8")
        lines = content.splitlines()
        section, error = locate_section(lines, mod_heading)
        if error:
            return False, error, None
        start, end = section
        wanted_action = clean(action)
        matches = []
        for i in range(start + 1, end):
            line = lines[i]
            if not line.startswith("|"):
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) >= 5 and clean(cells[0]) == wanted_action:
                matches.append((i, cells))
        if len(matches) != 1:
            return False, "Could not find one unique test-action row. Copy the complete action text from the selected mod's table.", None
        row_index, cells = matches[0]
        if cells[1].casefold() not in {"not tested", "pending", "not recorded", ""}:
            return False, f"This checklist action already has the result {cells[1]}. The automation will not overwrite an existing result; a maintainer must review this retest.", None
        cells[1] = md_cell(result)
        cells[2] = md_cell(tester)
        cells[3] = md_cell(date)
        cells[4] = md_cell(evidence) + f" (submitted in issue #{ISSUE_NUMBER})"
        lines[row_index] = "| " + " | ".join(cells[:5]) + " |"
        new_content = "\n".join(lines) + ("\n" if content.endswith("\n") else "")
        try:
            commit = api("PUT", path, {
                "message": f"Record beta test result from issue #{ISSUE_NUMBER}",
                "content": base64.b64encode(new_content.encode("utf-8")).decode("ascii"),
                "sha": file_info["sha"], "branch": "main",
            })
            return True, "Checklist row updated.", commit.get("commit", {}).get("html_url")
        except urllib.error.HTTPError as exc:
            if exc.code in {409, 422} and attempt < 3:
                time.sleep(1 + attempt)
                continue
            raise
    return False, "The checklist changed while this result was being saved. Please ask the maintainer to retry.", None

def main():
    event = json.loads(Path(EVENT_PATH).read_text(encoding="utf-8"))
    body = event.get("issue", {}).get("body") or ""
    tester = field(body, "Your full name")
    date = field(body, "Test date")
    mod = field(body, "Exact mod section heading")
    action = field(body, "Exact test action")
    result = field(body, "Test result")
    evidence = field(body, "What happened? (required)")
    missing = [name for name, value in [
        ("Your full name", tester), ("Test date", date), ("Exact mod section heading", mod),
        ("Exact test action", action), ("Test result", result), ("What happened?", evidence),
    ] if not value]
    if missing:
        comment("I could not update the checklist because these form fields were missing: " + ", ".join(missing) + ". Please submit a corrected report.")
        return
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        comment("I could not update the checklist because the test date must use YYYY-MM-DD.")
        return
    try:
        from datetime import date as date_type
        date_type.fromisoformat(date)
    except ValueError:
        comment("I could not update the checklist because the test date is not a valid calendar date.")
        return
    if result not in {"Pass", "Partial", "Failed", "Blocked", "N/A"}:
        comment("I could not update the checklist because the result must be Pass, Partial, Failed, Blocked, or N/A.")
        return
    ok, message, commit_url = update_checklist(mod, action, result, tester, date, evidence)
    if not ok:
        comment("**Checklist not changed.** " + message + "\n\nPlease check the exact mod heading and test-action text, or ask the maintainer to review this submission.")
        return
    response = f"**Checklist updated automatically.** The result {result} for **{action}** under **{mod.lstrip('# ').strip()}** was recorded for **{tester}** on **{date}**."
    if commit_url:
        response += f"\n\n[View the checklist update commit]({commit_url})."
    comment(response)
    api("PATCH", f"/repos/{REPOSITORY}/issues/{ISSUE_NUMBER}", {"state": "closed", "state_reason": "completed"})

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"::error::Test-result automation failed: {type(exc).__name__}: {exc}")
        raise
