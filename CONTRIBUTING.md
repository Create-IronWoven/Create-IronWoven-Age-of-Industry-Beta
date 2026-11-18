# Beta Testing, Feedback, and Contributions

Thanks for helping test Create IronWoven: Age of Industry.

This repository is the public beta tester hub. It is for player feedback and testing records, not the pack's source code.

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CONTRIBUTING-0001","record_type":"beta_tester_hub_scope","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:59:11Z","migrated_at":"2026-11-13T13:59:11Z","source_ref":["Beta CONTRIBUTING.md — page purpose and repository role: public beta testing/feedback hub, not pack source code. Reviewed against Master Prompt repository roles and Beta tree scope."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->



<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CONTRIBUTING-0002","record_type":"beta_public_issue_visibility_and_author_identity","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:59:11Z","migrated_at":"2026-11-13T13:59:11Z","source_ref":["Beta CONTRIBUTING.md — every issue form is public on submission; title/body/answers/comments/attachments and the account that opened the issue are publicly visible. A nickname does not anonymize the issue author. Cross-checked against the current public functional-test form and Private Master Prompt public-issue safety policy."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CONTRIBUTING-0003","record_type":"beta_public_evidence_sanitization","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:59:11Z","migrated_at":"2026-11-13T13:59:11Z","source_ref":["Beta CONTRIBUTING.md — sanitize evidence before public attachment; remove personal identifiers/contact data, credentials, private server addresses, local paths and raw private configuration. Rotate/revoke a credential if it may have been exposed. Reviewed against current public form warnings and the Private privacy/publication boundary."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

## Privacy and public issue submissions

Every issue form in this repository creates a public GitHub issue. The title, answers, comments, and attachments are visible as soon as the issue is submitted. GitHub also displays the submitting account as the issue author; a nickname does not anonymize it. Forms cannot screen content before initial publication.

Inspect screenshots, logs, and files before attaching them. Remove real names, personal contact details, passwords, access tokens, private server addresses, local paths, raw private configuration, and other sensitive details. Share only short, relevant, sanitized evidence. If a credential may have been exposed, rotate or revoke it immediately.

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CONTRIBUTING-0004","record_type":"beta_single_action_and_exact_checklist_match","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:59:11Z","migrated_at":"2026-11-13T13:59:11Z","source_ref":["Beta CONTRIBUTING.md — submit one Functional Test Result issue per completed checklist action and copy the exact mod heading/version and exact action text. Cross-checked against functional-test-report.yml required fields and scripts/apply_test_result.py exact-heading/action matching."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CONTRIBUTING-0005","record_type":"beta_test_report_identity_environment_and_evidence_fields","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:59:11Z","migrated_at":"2026-11-13T13:59:11Z","source_ref":["Beta CONTRIBUTING.md — required tester nickname, actual test environment, DD-MM-YYYY date, result, and concise sanitized evidence. The public form requires these fields and warns not to enter a real name or GitHub account name. Form and private processor field validation were reviewed; no report was submitted."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

## Functional mod testing

Use the **Functional test result** issue form for a completed test action from the testing checklist.

- Submit **one form for each test action** you complete. Do not combine several actions into one report.
- Choose the environment in which you actually tested: **Single-player**, **Multiplayer**, or **Both**.
- Copy the mod's exact checklist heading, including its version, and the exact test-action text.
- Select the result and provide the test date in **DD-MM-YYYY** format.
- Use a nickname or pseudonym in the tester field. Do not enter your real name or GitHub username.
- Include concise observations and sanitized evidence. Remove account names, private file paths, IP addresses, tokens, and other personal information.

**Privacy notice:** GitHub publicly displays the account that opened an issue as its author. The form's nickname field does not hide or anonymize that GitHub account. Do not submit through the public issue form if you need your GitHub account identity to remain private.

The private processor validates reports before changing the checklist. The current organization-owned Beta route has verified a valid first checklist write (issue #12), exact duplicate handling without a checklist write (issue #11), and invalid-heading rejection without a checklist write (issue #10). A materially different retest is covered by unit tests, but its live end-to-end observation is deferred until a genuine retest is submitted. After submitting, check the checklist for the result; do not manually edit checklist rows or submit duplicate reports just because an update is not immediately visible. If processing fails or a report needs review, leave the issue open and follow the maintainer's instructions.

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CONTRIBUTING-0006","record_type":"beta_private_test_result_processor_and_no_overwrite_boundary","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:59:11Z","migrated_at":"2026-11-13T13:59:11Z","source_ref":["Beta CONTRIBUTING.md — public Beta forwards only repository, issue number and event action; the private processor fetches the authoritative public issue, validates its source/fields/exact checklist target, and does not overwrite an existing result. Checked against the live Beta forwarder, Private process-public-test-results workflow, scripts/apply_test_result.py and docs/PUBLIC_TEST_AUTOMATION.md."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CONTRIBUTING-0007","record_type":"beta_valid_test_result_submission_end_to_end_verification","created_at":"unknown","updated_at":"unknown","migrated_at":"2026-11-13T13:59:11Z","source_ref":["Beta CONTRIBUTING.md — valid unique submission updating a matching checklist row, posting the success comment, and closing the issue remains pending end-to-end verification. docs/PUBLIC_TEST_AUTOMATION.md explicitly lists these positive-write, duplicate, and retest checks as still required. No test-result issue was submitted and no checklist row was changed during this chronology migration."],"timezone_display":"Europe/Amsterdam","chronology_status":"HISTORICAL"}
-->



<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CONTRIBUTING-0008","record_type":"beta_bug_feedback_categories_and_reproduction_details","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:59:11Z","migrated_at":"2026-11-13T13:59:11Z","source_ref":["Beta CONTRIBUTING.md — standard issue categories include bugs/crashes/reproducible problems, dedicated-server/multiplayer compatibility, mod conflicts/performance, questions/suggestions; the page requests relevant Minecraft/pack versions, environment, reproduction steps, expected and actual behavior. Current issue/reporting scope reviewed against Beta issue forms and Known Issues."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

## Bugs, crashes, and other feedback

Use the closest standard GitHub Issue form for:

- Bugs, crashes, and reproducible problems.
- Dedicated-server or multiplayer compatibility issues.
- Mod conflicts and performance problems.
- Questions and suggestions for features, mods, or balance.

Search existing issues first and include the Minecraft version, modpack version, environment, steps to reproduce, expected behavior, and actual behavior where relevant. Attach only sanitized screenshots or short log excerpts.

<!-- IRONWOVEN_CHRONOLOGY
{"record_id":"IRONWOVEN-BETA-CONTRIBUTING-0009","record_type":"beta_public_repository_submission_boundaries","created_at":"unknown","updated_at":"unknown","verified_at":"2026-11-13T13:59:11Z","migrated_at":"2026-11-13T13:59:11Z","source_ref":["Beta CONTRIBUTING.md — the Beta hub accepts feedback and test reports, not mod JARs, world saves, private configs, large log bundles, or direct checklist edits; feature suggestions are welcome but not guaranteed acceptance. Checked against Master Prompt public repository role and current Beta file layout."],"timezone_display":"Europe/Amsterdam","chronology_status":"CURRENT"}
-->

## Scope and repository boundaries

This is a player feedback and beta testing repository, not the pack's source code repository. Please do not submit mod JARs, world saves, private configuration files, or large log bundles. Do not edit the testing checklist directly; submit results through the designated form. Feature suggestions are welcome, but not every suggestion will be accepted.

<!-- IRONWOVEN_CHRONOLOGY
{
  "record_id": "IRONWOVEN-BETA-CONTRIBUTING-TEST-AUTOMATION-20261118-0001",
  "record_type": "current_beta_test_result_automation_verification",
  "created_at": "unknown",
  "updated_at": "2026-11-18T04:39:24Z",
  "verified_at": "2026-11-18T04:39:24Z",
  "source_ref": [
    "Beta issue #12 and forwarder/private processor runs 44232736737 / 44232749911 verify a valid first checklist write and completed issue closure.",
    "Beta issue #11 and forwarder/private processor runs 44231996038 / 44232007075 verify exact duplicate handling and no checklist change.",
    "Beta issue #10 and forwarder/private processor runs 42432977973 / 42432985663 verify invalid-heading rejection through the current organization-owned Beta route.",
    "The current private processor unit suite covers materially different retests; live end-to-end retest observation remains deferred until a genuine retest report is submitted.",
    "The prior CONTRIBUTING record IRONWOVEN-BETA-CONTRIBUTING-0007 is retained as HISTORICAL because its awaiting-first-write statement was superseded by the verified issue #12 event."
  ],
  "timezone_display": "Europe/Amsterdam",
  "chronology_status": "CURRENT"
}
-->
