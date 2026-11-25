# 01 Requirements for Libraries

Part of the Secure Development Requirements for Libraries, version 0.7 (draft), 2026-11-25. Read the
[README](README.md) first: it gives the wording rules, the working model, the terms and the sources.

## Scope

Applies to every repository in this set: it publishes a library, package, plug-in or other component
that other software builds on, and it is maintained voluntarily (however many volunteers take part).
These are all the requirements of the set. Meeting them meets OSPS Baseline Level 1 (README, section
8). Document 02 gives code agents detailed guidance on how to do the work well; it is not a
checklist.

Each requirement says **who** does it: the **person** (the owner), an **agent**, or **CI**
(automated checks that agents set up and that then run by themselves). Most of the person's part is
done once per repository; the section "The Person's Part" lists all of it.

## Requirements

### Ownership and Public Record (GOV)

- **GOV-01 (MUST) Named owner (a person).** The repository has a named owner who is accountable for
  its security and for meeting these requirements, and a named deputy where one exists. The owner is
  a person, never a code agent, and stays accountable for work done by agents. *Who:* person, once.
  *Evidence:* owner named in `SECURITY.md` or `CODEOWNERS`, in a public repository by public handle.
  *OSPS Level 1:* OSPS-VM-02.01 (with VUL-01). *Sources:* ISO 27001 A.5.2, A.5.8; SSDF PO.2; IEC
  62443-4-1 SM.
- **GOV-03 (MUST) Set and version recorded.** The repository records that it follows this set, and
  which version of it. The set is referenced, not copied: the record names this set's central
  repository, the version tag and the commit hash of that tag (README, "Using This Set"). *Who:*
  agent, once and when the set changes. *Evidence:* the reference in the repository's README or
  `SECURITY.md`, and the filled-in checklist of this document in the repository. *Sources:* ISO
  27001 A.8.25, A.5.37.
- **GOV-09 (MUST) Public compliance record.** In a public repository, the filled-in checklist is
  published, so that compliance can be shown. It gives the status of each requirement and links to
  public evidence only. It MUST NOT contain: details of weaknesses that are not yet fixed (what is
  missing, where, or how it could be used), vulnerability details before the fix is released
  (VUL-09), names of people other than public maintainer handles, contact details other than the
  security contact, internal host names or network details, names of secrets, account or key
  identifiers, or which customers, programmes or organisations use the software. For a requirement
  that is not met, the public line says only "not met" and a target date; the reason and the plan
  are kept in a private record (README, section 3). *Who:* agent writes it; the person agrees it
  when it is first published. *Sources:* ISO 27001 A.5.12, A.5.14, A.8.12; ISO/IEC 29147.
- **GOV-10 (MUST) No user or sector information in public repositories.** Public repositories,
  including documents, examples, test data, issue templates and agent instruction files, do not name
  customers, programmes, sectors or organisations that use the software, unless that user has agreed
  to be named in public. Only general standards are cited, never sector-specific ones, because the
  choice of sector standards shows who the users are. *Who:* agent, checked in every review
  (SRC-05). *Sources:* ISO 27001 A.5.12, A.8.12.

### Repository (SRC)

- **SRC-02 (MUST) Least-privilege repository access.** New collaborators get no rights, or the
  lowest rights, until rights are assigned by hand. Write access only for people who need it, admin
  access for as few people as possible, and access removed when someone leaves the work. Access is
  checked when someone is given it or leaves the work; no periodic review is needed. *Who:* person,
  only when access changes. *Evidence:* the platform's access settings. *OSPS Level 1:*
  OSPS-AC-02.01. *Sources:* ISO 27001 A.5.15, A.5.18, A.8.2, A.8.4; OSPS Baseline (Access Control).
- **SRC-03 (MUST) Multi-factor authentication.** Every account with write access to the repository,
  the CI system or a package registry uses multi-factor authentication. *Who:* person, once.
  *Evidence:* hosting platform setting. *OSPS Level 1:* OSPS-AC-01.01. *Sources:* ISO 27001 A.8.5;
  OSPS Baseline (Access Control); SSDF PO.5.
- **SRC-04 (MUST) Protected main branch.** The main branch, and any release branches, are protected:
  no direct pushes, no force pushes, no deletion. Changes arrive only through a merge request whose
  required checks passed: the tests (TST-01), secret scanning (SRC-08), the vulnerability scan
  (DEP-05) and the review (SRC-05). Where all changes are pushed with one person's account, the
  protection requires the review as a check, not as an approval, because the hosting platform does
  not let an account approve its own merge request. *Who:* person, once. *Evidence:* branch
  protection settings. *OSPS Level 1:* OSPS-AC-03.01, OSPS-AC-03.02. *Sources:* ISO 27001 A.8.4,
  A.8.32; SSDF PS.1; OSPS Baseline (Access Control); SLSA source track.
- **SRC-05 (MUST) Every change reviewed by another session.** Every change to the main branch is
  reviewed before it is merged by a reviewer other than its author: a separate code agent session,
  or a person. The review follows document 02, section 3, and checks correctness, security, the
  public text rules (GOV-09, GOV-10) and that no check was weakened (AGT-06). Its result is recorded
  on the merge request as a comment that names the reviewer (a person, or an agent session and its
  model) and lists the findings and how each was answered, and is reported as the review check of
  SRC-04, set as a result of the review and never by the session that wrote the change. A change to
  CI workflows, to publishing or signing configuration, or to the agent instruction and permission
  files is also approved by the person before it is merged. *Who:* agent; the person only for the
  changes named in the last sentence. *Evidence:* review comments and check results on merge
  requests. *Sources:* ISO 27001 A.8.28, A.8.32; SSDF PW.7; IEC 62443-4-1 SI, SVV; ISO/IEC 20246.
- **SRC-07 (MUST NOT) No secrets in repository or files.** Secrets MUST NOT be stored in the
  repository, in its history, in build or start scripts, in configuration or environment files, in
  logs or in test data. Secrets come at run time from a secret manager, an operating-system key
  store, or the CI system's protected secrets. *Who:* agent; CI checks it (SRC-08). *Evidence:*
  secret scanning is clean. *OSPS Level 1:* OSPS-BR-07.01. *Sources:* ISO 27001 A.5.17, A.8.4; SSDF
  PS.1; ASVS 5.0 (Configuration).
- **SRC-08 (MUST) Secret scanning.** Secret scanning runs on every push, as a check that must pass
  before a merge, and on the whole history at least once. A secret that is found is treated as
  leaked: it is revoked and replaced first, then removed from the code. Removing it from history
  alone is not enough. *Who:* CI, set up once by an agent (and by the person where it is a platform
  setting); the person revokes a leaked secret. *Evidence:* scanner configuration and results. *OSPS
  Level 1:* OSPS-BR-07.01. *Sources:* ISO 27001 A.8.12; SSDF PS.1; OSPS Baseline.

### Dependencies (DEP)

- **DEP-01 (MUST) Trusted dependency sources.** Dependencies are obtained only from defined, trusted
  sources (for example the official package registry), over authenticated, encrypted connections,
  and an internal or private group name can never be supplied by a public repository. Local
  repositories (for example a developer's local Maven repository) are not used in release builds.
  *Who:* agent, once; CI keeps it. *Evidence:* repository configuration in the build. *Sources:* ISO
  27001 A.5.21; SSDF PO.3, PW.4; SLSA.
- **DEP-02 (MUST) Pinned and verified dependencies.** The library's own build uses fixed dependency
  versions (no version ranges, no "latest", no snapshots in releases) and verifies a checksum or
  signature of every downloaded artefact, using a lock file or a dependency verification file kept
  in the repository. The repository contains the list of direct dependencies (for example the
  version catalogue or package manifest). This covers build plug-ins and CI actions (pinned by
  commit hash). The versions the library declares in its published metadata state what it is
  compatible with and are not strict pins, unless a strict version is needed for a recorded reason,
  so that users can take security updates of shared dependencies. *Who:* agent; CI enforces it.
  *OSPS Level 1:* OSPS-QA-02.01. *Sources:* SSDF PW.4, PS.2; SLSA; OWASP SCVS.
- **DEP-03 (MUST) New dependencies checked and approved.** A new direct dependency is checked before
  it is added (document 02, section 6: need, maintenance, known vulnerabilities, licence, its own
  dependencies, and that it exists under that exact name in the registry). The person approves each
  new direct runtime dependency, usually after reading the agent's check in the merge request; a new
  test-only or build-only dependency is approved by the review. *Who:* agent checks; the person
  approves runtime dependencies (rare). *Evidence:* check and approval in the merge request.
  *Sources:* ISO 27001 A.5.19, A.5.21; SSDF PW.4.1; OWASP SCVS; ISO/IEC 18974.
- **DEP-05 (MUST) Vulnerability scanning.** All dependencies, direct and transitive, are scanned for
  known vulnerabilities on every change, as a check that must pass before a merge, and at least
  weekly, against a public vulnerability database (for example OSV). A finding is fixed by an
  update, or has a short recorded assessment that the library is not affected. *Who:* CI, set up
  once by an agent; agents propose the updates. *Evidence:* scan results. *Sources:* ISO 27001
  A.8.8; SSDF RV.1, RV.2; EU CRA Annex I Part II.
- **DEP-08 (MUST) Open source licence, dependency licences known.** The library's licence meets the
  OSI Open Source Definition or the FSF Free Software Definition (for example Apache-2.0), is kept
  in a `LICENSE` or `COPYING` file in the repository, and is included in each released artefact or
  alongside it. The licences of all dependencies are known and compatible with the library's own
  licence, and notices required by the licences of its dependencies are delivered with it. *Who:*
  agent; checked in the review of DEP-03. *OSPS Level 1:* OSPS-LE-02.01, OSPS-LE-02.02,
  OSPS-LE-03.01, OSPS-LE-03.02. *Sources:* ISO 27001 A.5.32; ISO/IEC 5230 (OpenChain); OSPS Baseline
  (Legal).
- **DEP-09 (MUST) SBOM per release.** A software bill of materials (SBOM) in a standard format
  (CycloneDX or SPDX) is produced by the build for every release and published with it. It lists all
  components with name, version, supplier, licence, a unique identifier (for example a package URL)
  and a hash. *Who:* CI, set up once by an agent. *Sources:* SSDF PS.3.2; EU CRA Annex I Part II
  (1); BSI TR-03183-2; OWASP SCVS.

### Build and Publishing (BLD, LIB)

- **BLD-02 (MUST) Releases built in CI.** Releases are built by the CI system on a hosted build
  platform, not on a personal computer. *Who:* CI, set up once by an agent. *Sources:* SLSA Build
  L2; SSDF PO.5.
- **BLD-04 (MUST) Least-privilege CI.** CI jobs run with the least privileges they need, and never
  trust what others can write: tokens are read-only by default, write and publishing rights are
  given only to the release job, and secrets are not available to jobs started from untrusted
  contributions (for example merge requests from forks). Values that others can set (branch names,
  tags, commit messages, merge request titles and descriptions, author names) are quoted or
  validated before a pipeline uses them, and are never put directly into a shell command. *Who:*
  agent writes the workflows; the person approves them (SRC-05). *OSPS Level 1:* OSPS-BR-01.01,
  OSPS-BR-01.03. *Sources:* SSDF PO.5; OSPS Baseline (Build and Release).
- **BLD-06 (MUST) Signed artefacts with checksums.** Release artefacts are signed and published with
  checksums, so that users can check that what they received is what was built. Signing keys are
  kept only in the CI system's protected secrets or a key store, never in the repository. *Who:*
  person creates the key and puts it in CI secrets, once; CI signs. *Sources:* SSDF PS.2; ISO 27001
  A.8.24; EU CRA Annex I Part I; SLSA.
- **LIB-01 (MUST) Published from CI by the person, with scoped credentials.** The library is
  published only to its official registry, only from the CI release job (BLD-02), and only when the
  person starts the release; agents prepare releases but never start them (AGT-05). Publishing
  credentials are held only by the CI system and the person, are scoped to this library, and use
  multi-factor authentication or short-lived tokens (for example trusted publishing). All official
  addresses of the library (repository, documentation, downloads) are reached only over encrypted,
  authenticated connections (HTTPS or SSH). *Who:* person sets up the credentials once, and starts
  each release (one action). *OSPS Level 1:* OSPS-BR-03.01, OSPS-BR-03.02. *Sources:* SSDF PS.2;
  SLSA; OSPS Baseline (Build and Release).
- **LIB-03 (MUST) Published versions never changed.** A published version is never changed or
  replaced. A faulty version is fixed by a new version and, where the registry allows, the faulty
  one is marked as such. *Who:* agent and person. *Sources:* SSDF PS.3; SLSA.

### Tests (TST)

- **TST-01 (MUST) Automated tests block merges.** Automated tests run in CI on every change, for
  every supported target, and a change is not merged while tests fail. Tests are not removed,
  skipped or weakened to make a change pass; a test that is wrong is fixed in a reviewed change with
  the reason recorded. A test that fails at random is quarantined only with the person's approval
  and an issue. *Who:* agent writes the tests; CI runs them. *Sources:* ISO 27001 A.8.29; SSDF PW.8.

### Vulnerabilities (VUL, LIB)

- **VUL-01 (MUST) Security policy.** The repository has a security policy (`SECURITY.md`) that says
  how to report a vulnerability privately, who receives reports, what response to expect (LIB-11),
  and which versions get security fixes. The reporting channel is the hosting platform's private
  vulnerability reporting or a dedicated security address, not a personal address. *Who:* agent
  writes it; the person turns on private reporting, once. *OSPS Level 1:* OSPS-VM-02.01. *Sources:*
  EU CRA Annex I Part II (5, 6); ISO/IEC 29147; OSPS Baseline (Vulnerability Management); SSDF
  RV.1.3.
- **LIB-11 (MUST) Response expectations stated.** The security policy states honestly what users can
  expect: reports are handled on a best-effort basis, and no response or fix time is guaranteed.
  Users that need guaranteed times deal with vulnerabilities in the library in their own product.
  Where support for the library is ever offered commercially, the full requirements apply instead
  (README, section 2). *Who:* agent writes it. *Sources:* ISO/IEC 29147; OSPS Baseline
  (Vulnerability Management).
- **VUL-05 (MUST) Security advisories.** When a vulnerability is fixed, users are told in a security
  advisory: the affected versions, the fixed version, the severity and what users should do. Where
  the EU Cyber Resilience Act applies to the library, its reporting duties are followed. *Who:*
  agent drafts it; the person publishes it. *Sources:* EU CRA Article 14, Annex I Part II (4);
  ISO/IEC 29147.
- **VUL-09 (MUST) Coordinated disclosure.** Details of a vulnerability are not made public (in
  issues, commits, merge request texts, release notes or the checklist) until a fixed release is
  available, or until a disclosure date agreed with the reporter. Fixes for vulnerabilities that are
  not yet public are prepared in a private workspace (for example the hosting platform's private
  advisory fork), and the public commit message does not describe how to exploit the fault. *Who:*
  agent and person. *Sources:* ISO/IEC 29147, 30111; EU CRA Annex I Part II; SSDF RV.2.

### Library Behaviour (LIB)

- **LIB-07 (MUST NOT) No hidden network use or telemetry.** The library MUST NOT send data over the
  network, write outside the locations given by its caller, or collect telemetry, unless that is its
  documented purpose. *Who:* agent; checked in every review. *Sources:* EU CRA Annex I Part I; GDPR
  Article 25.

### Open Source Project (LIB)

- **LIB-12 (MUST) Public repository and history.** The source repository is publicly readable at a
  stable address, with a public record of every change, who made it and when. History is not
  rewritten in a way that hides who made a change. *Who:* person, once (a public repository). *OSPS
  Level 1:* OSPS-QA-01.01, OSPS-QA-01.02.
- **LIB-13 (MUST) User guide.** After each release, the documentation includes a user guide for all
  basic functions: how to install, configure and use the library, with clearly visible warnings on
  options that are dangerous. *Who:* agent. *OSPS Level 1:* OSPS-DO-01.01.
- **LIB-14 (MUST) Defect reporting and public discussion.** The documentation says how to report a
  defect (normally the repository's issue tracker) and what to expect, on a best-effort basis
  (LIB-11). There is a public place to discuss proposed changes and problems with using the library
  (normally the same issue tracker). *Who:* agent writes it; the person keeps the issue tracker
  turned on. *OSPS Level 1:* OSPS-DO-02.01, OSPS-GV-02.01.
- **LIB-15 (MUST) Contribution statement.** A `CONTRIBUTING.md` file explains how to contribute, or
  says clearly that public contributions are not accepted. *Who:* the person decides which, once; an
  agent writes it. *OSPS Level 1:* OSPS-GV-03.01.
- **LIB-16 (MUST NOT) No binaries in the repository.** The repository MUST NOT contain generated
  executables, or binary files that cannot be reviewed (compiled code, libraries, archives of them).
  Images, sounds and similar assets are allowed. Binaries needed for tests are generated by the
  build, or fetched in a documented build step. A build tool wrapper (for example
  `gradle-wrapper.jar`) is kept only if CI checks it against the checksum its publisher publishes
  (A1, KMP-06); this is this set's reading of OSPS-QA-05.02, which does not mention wrappers. *Who:*
  agent; checked in every review. *OSPS Level 1:* OSPS-QA-05.01, OSPS-QA-05.02.
- **LIB-17 (MUST) Repositories listed.** Where the library is built from more than one repository,
  the documentation lists them, with what each is for. *Who:* agent. *OSPS Level 1:* OSPS-QA-04.01.

### Code Agents (AGT)

- **AGT-03 (MUST) Agents sandboxed, least privilege.** Agents run in a sandbox or a separate
  environment, with access only to the repositories of the task, with no access to production
  systems, production data or publishing and signing credentials, and with network access limited to
  what the task needs. *Who:* person sets up the environment, once. *Sources:* ISO 27001 A.8.2,
  A.8.31; SSDF PO.5.
- **AGT-05 (MUST NOT) No changes to protected settings or releases.** Agents MUST NOT change the
  settings of the repository, the CI system or the registry (branch protection, access rights,
  secrets, signing and publishing credentials, agent permissions), push directly to the main branch,
  start or publish releases, publish advisories, or approve their own merge requests. They MAY
  propose any of these to the person. *Who:* agent. *Sources:* ISO 27001 A.5.3, A.8.32.
- **AGT-06 (MUST NOT) No weakening of checks.** Agents MUST NOT disable, skip or weaken tests,
  security checks, warnings or verification files (for example dependency checksums) to make a
  change pass. If they cannot make a check pass, they report it. *Who:* agent; checked in every
  review. *Sources:* ISO 27001 A.8.29; SSDF PW.8.
- **AGT-18 (MUST) Agents keep private context out of public text.** Agents working on a public
  repository apply GOV-09 and GOV-10 to everything they write there: code, comments, commit
  messages, merge request texts, issue comments and generated documents. Context they were given
  privately (names of other projects, users, people, internal systems, private tasks) does not
  appear in public text. A gap assessment (adoption guide) is not posted in a public issue or merge
  request. *Who:* agent. *Sources:* ISO 27001 A.5.14, A.8.12.

## The Person's Part

Everything else is done by agents or runs in CI. The adoption guide gives the steps in order.

**Once per repository** (about an hour, most of it on the hosting platform's settings pages):

- Name yourself as owner (GOV-01) and turn on multi-factor authentication for every account that can
  write (SRC-03).
- Protect the main branch with the required checks (SRC-04).
- Turn on private vulnerability reporting (VUL-01), keep the issue tracker on (LIB-14), decide
  whether public contributions are accepted (LIB-15) and, where it is a platform setting, secret
  scanning (SRC-08).
- Create the signing key and the publishing credentials, and put them in the CI system's protected
  secrets, or set up trusted publishing (BLD-06, LIB-01).
- Set up the agent environment so that agents have no publishing or signing credentials (AGT-03).
- Agree the first public checklist (GOV-09).

**When it happens:**

- Approve a new direct runtime dependency (DEP-03).
- Approve a change to CI workflows, publishing or signing configuration, or agent instructions and
  permissions (SRC-05).
- Start a release (LIB-01).
- Revoke and replace a secret that has leaked (SRC-08).
- Handle a vulnerability report on a best-effort basis, and publish the advisory that an agent
  drafted (VUL-05, VUL-09).
- Approve quarantining a test that fails at random (TST-01).

**When access changes:** give the lowest rights needed, and remove them when someone leaves
(SRC-02).

## Checklist

Status: **met**, **partly**, **not met**, **n/a**. A "not met" or "n/a" needs a short reason, kept
in the private record for a public repository (GOV-09). In a public repository, the evidence column
gives status, public links and target dates only.

| Id | Level | Requirement | Status | Evidence or reason |
|----|-------|-------------|--------|--------------------|
| GOV-01 | MUST | Named owner (a person) | | |
| GOV-03 | MUST | Set and version recorded | | |
| GOV-09 | MUST | Public compliance record | | |
| GOV-10 | MUST | No user or sector information in public repositories | | |
| SRC-02 | MUST | Least-privilege repository access | | |
| SRC-03 | MUST | Multi-factor authentication | | |
| SRC-04 | MUST | Protected main branch | | |
| SRC-05 | MUST | Every change reviewed by another session | | |
| SRC-07 | MUST NOT | No secrets in repository or files | | |
| SRC-08 | MUST | Secret scanning | | |
| DEP-01 | MUST | Trusted dependency sources | | |
| DEP-02 | MUST | Pinned and verified dependencies | | |
| DEP-03 | MUST | New dependencies checked and approved | | |
| DEP-05 | MUST | Vulnerability scanning | | |
| DEP-08 | MUST | Open source licence, dependency licences known | | |
| DEP-09 | MUST | SBOM per release | | |
| BLD-02 | MUST | Releases built in CI | | |
| BLD-04 | MUST | Least-privilege CI | | |
| BLD-06 | MUST | Signed artefacts with checksums | | |
| LIB-01 | MUST | Published from CI by the person, with scoped credentials | | |
| LIB-03 | MUST | Published versions never changed | | |
| TST-01 | MUST | Automated tests block merges | | |
| VUL-01 | MUST | Security policy | | |
| LIB-11 | MUST | Response expectations stated | | |
| VUL-05 | MUST | Security advisories | | |
| VUL-09 | MUST | Coordinated disclosure | | |
| LIB-07 | MUST NOT | No hidden network use or telemetry | | |
| LIB-12 | MUST | Public repository and history | | |
| LIB-13 | MUST | User guide | | |
| LIB-14 | MUST | Defect reporting and public discussion | | |
| LIB-15 | MUST | Contribution statement | | |
| LIB-16 | MUST NOT | No binaries in the repository | | |
| LIB-17 | MUST | Repositories listed | | |
| AGT-03 | MUST | Agents sandboxed, least privilege | | |
| AGT-05 | MUST NOT | No changes to protected settings or releases | | |
| AGT-06 | MUST NOT | No weakening of checks | | |
| AGT-18 | MUST | Agents keep private context out of public text | | |
