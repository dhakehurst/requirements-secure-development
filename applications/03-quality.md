# 03 Quality Requirements

Part of the Secure Development Requirements for Applications, version 0.5 (draft), 2026-11-25. Read
the [README](README.md) first: it gives the wording rules, the working model, the terms and the
sources.

## Scope

Applies to every repository. These requirements cover software quality beyond security: that the
software does what it is specified to do, reliably, and that it can be maintained. Security
requirements on testing and review are in the core document and are not repeated here.

## Requirements

### Quality Requirements and Planning (QPL)

- **QPL-01 (MUST) Quality requirements stated.** The quality requirements of the software are
  written down, using the product quality characteristics of ISO/IEC 25010 that matter for it
  (functional suitability, performance efficiency, compatibility, interaction capability,
  reliability, security, maintainability, flexibility, safety), each with a measurable target where
  possible. *Evidence:* quality requirements section. *Sources:* ISO/IEC 25010:2023; ISO/IEC/IEEE
  12207 (stakeholder needs and requirements definition); ISO 9001 8.2.
- **QPL-02 (SHOULD) Functional requirements recorded.** What the software does is recorded as
  requirements (or as user stories with acceptance criteria) that can be tested, each with a stable
  id. Where document 07 applies, this is a MUST (TQS-02). *Evidence:* requirements in the repository
  or a linked tracker. *Sources:* ISO/IEC/IEEE 12207; ISO/IEC/IEEE 29148; ISO 9001 8.3.3.
- **QPL-03 (MUST) Supported platforms stated.** The supported platforms, runtimes and versions (for
  example operating systems, runtime versions and compilation targets) are stated, and each one is
  built and tested in CI. *Evidence:* platform list and CI matrix. *Sources:* ISO/IEC 25010
  (compatibility, flexibility); ISO/IEC/IEEE 12207.
- **QPL-04 (MUST) Test strategy.** A short test strategy says which test levels are used (unit,
  integration, system, acceptance), what each covers, which are automated, and what must pass before
  a merge and before a release. *Evidence:* test strategy in the developer guide. *Sources:*
  ISO/IEC/IEEE 29119-2, 29119-3; ISO/IEC/IEEE 12207 (verification, validation).
- **QPL-05 (SHOULD) Quality targets for code.** Targets are set for test coverage and for code
  measures (for example complexity, duplication, size of functions), and are checked automatically.
  *Sources:* ISO/IEC 5055; ISO/IEC 25023.

### Traceability and Configuration (QCM)

- **QCM-01 (SHOULD) Requirements traced to tests.** Each requirement (QPL-02 and the security
  requirements of the core document) is linked to the tests that verify it, and the links can be
  listed per release. Where document 07 applies, this is a MUST (TQS-04). *Evidence:* trace list or
  tags in tests. *Sources:* ISO/IEC/IEEE 12207; ISO/IEC/IEEE 29119-3; ISO 9001 8.5.2.
- **QCM-02 (MUST) Configuration items identified.** Everything that makes up a release (source,
  build scripts, dependencies, configuration, documentation) is identified, versioned and recorded
  for each release. *Sources:* ISO/IEC/IEEE 12207 (configuration management); ISO 9001 8.5.2; ISO
  27001 A.8.9.
- **QCM-03 (MUST) Known problems list.** A list of known problems is kept and published with each
  release: what goes wrong, the affected versions, and any workaround. *Evidence:* issue tracker
  filter or known-problems file. *Sources:* ISO 9001 8.7, 10.2; ISO/IEC/IEEE 12207 (problem
  resolution).

### Construction and Review (QCR)

- **QCR-01 (MUST) Coding conventions.** Coding conventions are adopted and enforced automatically
  (formatter and linter in CI), so that reviews can concentrate on content. *Sources:* ISO/IEC/IEEE
  12207 (implementation); ISO/IEC 5055.
- **QCR-02 (MUST) Review covers quality.** The review of each change (core SRC-05) also checks: that
  it meets its requirement, that tests were added or changed to match, that documentation was
  updated, and that it does not add needless complexity. *Sources:* ISO/IEC 20246 (work product
  reviews); ISO 9001 8.3.4.
- **QCR-03 (MUST) Regression test for each fault.** Every fixed fault gets a test that failed before
  the fix and passes after it. *Sources:* ISO/IEC/IEEE 29119; ISO 9001 10.2.
- **QCR-04 (MUST) Tests are deterministic.** Tests give the same result on every run. A test that
  fails at random is fixed, or quarantined in a change approved by a person, with an issue and a
  date; it is not ignored. *Sources:* ISO/IEC/IEEE 29119.
- **QCR-05 (SHOULD) Design reviewed before large changes.** A large or architecture-changing piece
  of work has a short written design (options and the chosen one), reviewed before implementation
  starts. *Sources:* ISO/IEC/IEEE 12207 (architecture and design definition); ISO 9001 8.3.4.

### Documentation (QDO)

- **QDO-01 (MUST) User documentation.** The software has user documentation that matches the
  released version: how to install, configure and use it, and its limitations. *Sources:*
  ISO/IEC/IEEE 26514; ISO/IEC 25010 (interaction capability).
- **QDO-02 (MUST) Developer documentation.** The repository has developer documentation:
  architecture overview, how to build and test, code structure, and design decisions with their
  reasons. *Sources:* ISO/IEC/IEEE 12207; ISO/IEC/IEEE 42010 (architecture description).
- **QDO-03 (MUST) API documentation.** Public APIs are documented in the code (purpose, parameters,
  results, errors), and the documentation is generated in the build. *Sources:* ISO/IEC 25010
  (maintainability).
- **QDO-04 (retired in 0.3).** Merged into BLD-10.

### Release and Improvement (QRI)

- **QRI-01 (MUST) Release criteria.** A release is made only when the release criteria are met: all
  tests pass on all supported platforms (QPL-03), the quality targets (QPL-05) are met or have a
  recorded exception, the documentation (QDO-01 to QDO-03, BLD-10) is updated, and the known
  problems list is up to date. *Sources:* ISO 9001 8.6; ISO/IEC/IEEE 29119-2 (test completion).
- **QRI-02 (MUST) User problem reports handled.** Problem reports from users are recorded, answered,
  classified (fault, question, wish) and tracked until closed. *Sources:* ISO 9001 8.2.1, 10.2;
  ISO/IEC/IEEE 12207 (problem resolution).
- **QRI-03 (MUST) Deprecation before removal.** Features and APIs are marked as deprecated, with the
  replacement, at least one release before they are removed. *Sources:* ISO/IEC 25010
  (compatibility).
- **QRI-04 (SHOULD) Regular improvement.** At least twice a year the owner looks at faults found,
  review findings, failed releases and user reports, and changes the process where the same kind of
  problem recurs. *Sources:* ISO 9001 10.1; ISO/IEC 33001 (process assessment).
- **QRI-05 (SHOULD) Accessibility.** Graphical user interfaces meet WCAG 2.1 level AA (the level EN
  301 549 refers to), or WCAG 2.2 level AA, where it applies (for example keyboard use, contrast,
  text alternatives, scaling). *Sources:* EN 301 549; WCAG 2.1, 2.2.
- **QRI-06 (retired in 0.3).** Merged into BLD-11.

## Checklist

Status: **met**, **partly**, **not met**, **n/a**. Every "not met" MUST and every "n/a" needs a
short reason; a "not met" MUST also needs an exception (GOV-05). In a public repository, the
evidence column follows GOV-09: status, public links and target dates only.

| Id | Level | Requirement | Status | Evidence or reason |
|----|-------|-------------|--------|--------------------|
| QPL-01 | MUST | Quality requirements stated | | |
| QPL-02 | SHOULD | Functional requirements recorded | | |
| QPL-03 | MUST | Supported platforms stated | | |
| QPL-04 | MUST | Test strategy | | |
| QPL-05 | SHOULD | Quality targets for code | | |
| QCM-01 | SHOULD | Requirements traced to tests | | |
| QCM-02 | MUST | Configuration items identified | | |
| QCM-03 | MUST | Known problems list | | |
| QCR-01 | MUST | Coding conventions | | |
| QCR-02 | MUST | Review covers quality | | |
| QCR-03 | MUST | Regression test for each fault | | |
| QCR-04 | MUST | Tests are deterministic | | |
| QCR-05 | SHOULD | Design reviewed before large changes | | |
| QDO-01 | MUST | User documentation | | |
| QDO-02 | MUST | Developer documentation | | |
| QDO-03 | MUST | API documentation | | |
| QRI-01 | MUST | Release criteria | | |
| QRI-02 | MUST | User problem reports handled | | |
| QRI-03 | MUST | Deprecation before removal | | |
| QRI-04 | SHOULD | Regular improvement | | |
| QRI-05 | SHOULD | Accessibility | | |
