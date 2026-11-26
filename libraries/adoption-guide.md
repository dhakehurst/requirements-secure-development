# Adoption Guide for Library Repositories

Part of the Secure Development Requirements for Libraries, version 0.8 (draft), 2026-11-26. Read the
[README](README.md) first: it gives the wording rules, the working model, the terms and the sources.

## Purpose

This guide says how to bring a library repository into line with document 01, in a way that code
agents can do nearly all of, and that needs the person for about an hour of settings, once. New
repositories follow the same steps before their first release.

## Step 1: Gap Assessment (Agent)

Give an agent session document 01, this guide and read access to the repository. It:

1. Fills in the checklist of document 01 from what it can see: build files, CI configuration, scan
   results, documentation and history, with the evidence (a file path, a setting, a link) for each
   "met".
2. Marks settings that it cannot see (multi-factor sign-in, branch protection, access lists, CI
   secrets, registry accounts, private vulnerability reporting) as "not checked", and lists them for
   the person. It does not guess.
3. Writes a list of tasks for step 3, and the list of person steps for step 2 that are still open.

It changes no code or setting in this step. In a public repository it does not post its findings in
a public issue, comment or merge request (AGT-18); the filled-in checklist and the task list go into
the private record until step 4.

## Step 2: The Person's Settings (Once)

These are the person's part of document 01 that is done once. On GitHub they are all on the
repository's and the account's settings pages.

1. Multi-factor authentication on every account that can write to the repository, the CI system or
   the registry (SRC-03).
2. Access: only the people who need it, and admin for as few as possible (SRC-02).
3. Private vulnerability reporting turned on (VUL-01).
4. Secret scanning and push protection turned on where the platform offers them (SRC-08). On GitHub
   they are free for public repositories.
5. CI token permissions read-only by default (BLD-04).
6. Signing key created and stored only in the CI system's protected secrets; publishing credentials
   scoped to this library in CI secrets, or trusted publishing set up (BLD-06, LIB-01).
7. Agent environment without publishing or signing credentials (AGT-03).
8. Issue tracker turned on, for defect reports and public discussion (LIB-14).
9. Decide whether public contributions are accepted; an agent writes the answer into
   `CONTRIBUTING.md` (LIB-15).
10. Branch protection on the main branch, requiring the checks of SRC-04, with deletion blocked. Do
    this after step 3 has added the checks, so that their names exist.

## Step 3: The Agents' Work

Each item is a separate, reviewed change. Agents MAY do them in any order, but the CI checks come
first so that the later changes are checked.

- CI workflows that quote or validate values that others can set before using them (BLD-04).
- CI workflow with the tests for every target (TST-01), secret scanning on every push and once over
  the whole history (SRC-08), the vulnerability scan (DEP-05), and the review check (SRC-05). A
  secret found in the history is reported to the person, who revokes and replaces it first.
- Dependencies pinned and verified, CI actions pinned by commit hash, only trusted repositories
  (DEP-01, DEP-02).
- SBOM produced by the build and published with each release (DEP-09).
- Release workflow: built in CI, signed, with checksums, publishing only from the release job,
  started by the person (BLD-02, BLD-06, LIB-01).
- `SECURITY.md` with the reporting channel, the "best effort" statement and the supported versions;
  owner named (GOV-01, VUL-01, LIB-11).
- Licence in a `LICENSE` file and included with each release, dependency licences checked, notices
  delivered (DEP-08). The repository contains the list of direct dependencies (DEP-02).
- User guide, how to report defects, `CONTRIBUTING.md`, and the list of repositories if there are
  several (LIB-13 to LIB-15, LIB-17).
- Binaries removed from the repository, or, for a build tool wrapper, checked by CI (LIB-16).
- A check that the library makes no hidden network calls, writes or telemetry (LIB-07).
- Agent instruction file pointing to documents 01 and 02 and, for Kotlin, annex A1 (document 02,
  section 1).
- The checklist, with the set's version (GOV-03), and the OSPS Baseline Level 1 claim (README,
  section 8).

The guidance of document 02 is not part of the adoption: agents apply it to every change from now
on, and improve existing code when they work on it.

## Step 4: Publish the Checklist

When the items of steps 2 and 3 are done, the person agrees the checklist and an agent commits it
(GOV-09). Anything still not met is "not met" with a target date, and its reason stays in the
private record.

## After Adoption

The person's ongoing part is listed in document 01, "The Person's Part": approve new runtime
dependencies and changes to CI, publishing or agent configuration; start releases; handle
vulnerability reports on a best-effort basis and publish advisories; approve quarantined tests;
set access when someone joins or leaves; and keep the issue tracker turned on. Everything else is
done by agents and CI.

## Prompts for the Agent

Copy these into the agent session, one step at a time. Replace `<URL of this repository>` with the
address of this requirements repository, `<commit>` with the full commit hash of the version to
follow (for example the latest commit of this repository's main branch), and `<x.y>` with the
version given at the top of the set's README at that commit.

Step 1, gap assessment:

```text
This repository will follow the Secure Development Requirements for Libraries, version <x.y>:
<URL of this repository>/tree/<commit>/libraries
Read README.md, 01-requirements.md, 02-agent-guidance.md and adoption-guide.md at that commit,
and A1-kotlin-multiplatform-annex.md if this repository uses Kotlin. Do not copy
them into this repository.

Do step 1 of the adoption guide (gap assessment) only:
- Fill in the checklist of document 01 from what you can see in the repository, with evidence
  for each "met".
- Mark settings you cannot see (MFA, branch protection, access, CI secrets, registry accounts,
  private vulnerability reporting) as "not checked". Do not guess.
- List the tasks for step 3 and the person steps for step 2 that are still open.
Change no code or settings, and post nothing public. Give me the checklist and both lists here.
```

Step 3, after the person has done the settings of step 2:

```text
Do step 3 of the adoption guide: one reviewed merge request per item, the CI checks first.
```

Step 4, when every item is met or has a target date:

```text
Do step 4 of the adoption guide: add the checklist, and the reference to the set (README of the
requirements repository, "Using This Set") to this repository's README.
```

## Private Repositories and Hosting Plans

Some hosting plans do not offer every feature for private repositories. For example, on GitHub (as
of November 2026), protected branches for the private repositories of a personal account need GitHub
Pro; secret scanning, push protection and code scanning for private repositories need paid add-ons
that are sold only with organisation plans; and CI minutes for private repositories are limited each
month. Branch protection has no workaround. Secret and dependency scanning can run as free tools in
CI (for example gitleaks and OSV-Scanner). Public repositories get these features without a paid
plan.
