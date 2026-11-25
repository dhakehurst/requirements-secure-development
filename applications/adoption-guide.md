# Adoption Guide for Existing Repositories

Part of the Secure Development Requirements for Applications, version 0.6 (draft), 2026-11-25. Read
the [README](README.md) first: it gives the wording rules, the working model, the terms and the
sources.

## Purpose

Most repositories exist before these requirements are applied to them. This guide says how to bring
an existing repository into line in stages, without stopping other work, and in a way that a code
agent can carry out. A repository that follows this guide is compliant from the first stage: every
requirement it does not yet meet has a recorded exception with a plan and a date (GOV-05).

New repositories start at stage 4: they meet the requirements from the first commit.

## Stage 1: Gap Assessment

1. Decide which documents apply (README, section 2), and whether a profile is used (the one-person
   profile), and record it (GOV-03).
2. Copy the checklists of those documents into the repository (for example
   `docs/security/compliance-checklist.md`).
3. Fill in each line from what can be seen in the repository: build files, CI configuration, scan
   results, documentation and history. Give the evidence (a file path, a setting, a link) for each
   "met".
4. Settings that are held by the hosting platform and not in the repository (multi-factor sign-in,
   branch protection, access lists, CI secrets, registry accounts) are checked by the owner, or by
   an agent that has been given read access to those settings for this purpose. An agent that cannot
   see a setting marks the line "not checked" and lists it for the owner; it does not guess.
5. For each MUST that is not met, write an exception (GOV-05) with a target stage and date.
6. The owner reviews and accepts the result.
7. In a private repository, the checklist and exceptions are committed. In a public repository, the
   gap list, the exceptions and the proposed tasks go into the private record (GOV-09); the public
   checklist, with status and target dates only, is committed after stage 2, so that it starts with
   few open items.

A code agent doing the assessment does not change any code or setting in this stage, and in a public
repository it does not post its findings in a public issue, comment or merge request (AGT-18). Its
output is the filled-in checklist, the exceptions, and a list of proposed tasks for stages 2 to 4.

## Stage 2: Quick Wins (Days)

These need little code and close the most common gaps. Each is a separate reviewed change.

- Owner named, `SECURITY.md` with a reporting channel and support statement (GOV-01, VUL-01).
- Agent instruction file that points to these requirements (AGT-01).
- Branch protection, multi-factor sign-in, least-privilege access and CI token rights (SRC-02 to
  SRC-04, BLD-04), with the review recorded as a required check (SRC-12). Done by the owner
  (SRC-06). Check first that the hosting plan provides them (see "Private Repositories and Hosting
  Plans").
- Secret scanning on every push, and once over the whole history. Any secret found is revoked and
  replaced first (SRC-07, SRC-08).
- Dependency versions pinned and verified, CI actions pinned by commit hash (DEP-02).
- Vulnerability scan and SBOM in CI (DEP-05, DEP-09).
- Formatter, linter and static analysis turned on in CI, with a baseline (see stage 3) so that they
  pass from the start; compiler warnings as errors turned on module by module (COD-08, TST-03,
  QCR-01).
- Repository backup set up (SRC-13), developer computers checked (SRC-14), and agent extensions in
  use listed and approved (AGT-19).

## Private Repositories and Hosting Plans

Some hosting plans do not offer every platform feature for private repositories. For example, on
GitHub (as of November 2026), protected branches for the private repositories of a personal account
need GitHub Pro; secret scanning, push protection, code scanning and dependency review for private
repositories need GitHub Secret Protection or GitHub Code Security, which are sold only with
organisation plans; and CI minutes for private repositories are limited each month. Check the plan
before stage 2. Where a feature is missing:

- Branch protection (SRC-04) has no workaround: use a plan that provides it, or record an exception.
- Secret scanning, static analysis and dependency scanning (SRC-08, TST-03, DEP-05) can run as free
  tools in CI (for example gitleaks, Semgrep or detekt, OSV-Scanner), within the CI minutes
  available. Builds for several targets use minutes quickly, so check that the minutes are enough
  before relying on them.
- On GitHub, public repositories get these features without a paid plan.

## Stage 3: New Changes Meet the Rules

From this stage, every new change meets the requirements, while existing problems are worked off.

- **Baselines.** Existing findings of static analysis, linters, compiler warnings and code measures
  are recorded in a baseline file committed to the repository. CI fails only on findings that are
  not in the baseline. The baseline may only shrink: a change that adds entries to it needs the same
  approval as an exception. Where a compiler has no baseline file (for example the Kotlin compiler,
  KMP-10), warnings as errors is turned on module by module, and the list of modules not yet
  switched is the baseline; it may only shrink.
- **Dependency vulnerabilities** already known are triaged at once and get fix dates under VUL-04,
  counted from the day of the assessment.
- **Changed code is brought up to standard.** When a change touches a file, findings in the code it
  changes are fixed in the same change or have an issue; tests are added for the behaviour it
  changes (QCR-03).
- **Process requirements** (reviews, change records, release checks, release notes) apply to every
  change and release from this stage.

## Stage 4: Catch-Up Work

The remaining gaps become ordinary tasks in the issue tracker, each linked to its exception, and are
worked on in this order (in a public repository, tasks that describe open security gaps are kept in
the private record, not in public issues) unless the owner decides otherwise:

1. Fix baseline findings of critical and high severity.
2. Write the threat model of the existing design (DES-02) and the security requirements (DES-01).
   Measures that the threat model shows to be missing become tasks.
3. Add tests for security-relevant code (TST-02) and requirements traceability (QCM-01).
4. Add fuzz tests for parsers of untrusted input (TST-05).
5. Bring the documentation up to date (PRD-02, QDO-01 to QDO-03).
6. Work off the rest of the baseline, by severity.

When an exception's work is done, the exception is closed and the checklist line becomes "met".

## Requirements That Apply Only Going Forward, or Only Once

- **Only going forward**: SBOM, provenance and signatures per release (DEP-09, BLD-06, BLD-07),
  release notes (BLD-10), review records (SRC-05). Earlier releases are not rebuilt to add them,
  unless a user needs it.
- **Once, looking back**: the secret scan of the whole history (SRC-08), the check that the
  repository holds no sensitive data (SRC-11), the licence check of existing dependencies and copied
  code (DEP-08, DEP-11).

## Working With Code Agents

A large part of this work suits code agents. Give each agent session one task from the list, with
this guide, the applicable documents and the current checklist. Follow the working model of the
README: one session writes the change, a separate session reviews it, and the owner approves
anything that changes security settings or makes a release. Keep changes small: one quick win or one
catch-up task per merge request.


