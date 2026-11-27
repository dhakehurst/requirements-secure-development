# 01 Core Secure Development Requirements

Part of the Secure Development Requirements for Applications, version 0.8 (draft), 2026-11-27. Read
the [README](README.md) first: it gives the wording rules, the working model, the terms and the
sources.

## Scope

Applies to every repository. Documents 02, 03 and 05 also always apply; documents 06, 07 and A1
apply as listed in the README.

## Requirements

### Governance (GOV)

- **GOV-01 (MUST) Named owner (a person).** The repository has a named owner who is accountable for
  its security and for meeting these requirements, and a named deputy where one exists. The owner is
  a person, never a code agent, and stays accountable for work done by agents. *Evidence:* owner
  named in the repository (for example `SECURITY.md` or `CODEOWNERS`), in a public repository by
  public handle or role. *Sources:* ISO 27001 A.5.2, A.5.8; SSDF PO.2; IEC 62443-4-1 SM.
- **GOV-02 (MUST) Process written down.** The development process is written down in the repository:
  how changes are made, reviewed, tested, built and released, and every change follows it. It MAY
  refer to these documents instead of repeating them. *Evidence:* `CONTRIBUTING.md` or a developer
  guide. *Sources:* ISO 27001 A.5.37, A.8.25, A.8.32; SSDF PO.1; OSPS Baseline (Documentation); IEC
  62443-4-1 SM; BSI CON.8.
- **GOV-03 (MUST) Applicable documents recorded.** The repository records which of these documents
  apply to it (README, section 2), and which version of them it follows. The set is referenced, not
  copied: the record names this set's central repository, the version and the full commit
  hash (README, "Using This Set"). *Evidence:* the reference in the repository's README or
  `SECURITY.md`, and the filled-in checklists of those documents in the repository. *Sources:* ISO
  27001 A.8.25, A.5.37.
- **GOV-04 (MUST) Checklist reviewed yearly and before major releases.** The checklist is reviewed
  before each major release and, where support for the application is offered commercially, also at
  least once a year. *Evidence:* date of last review in the checklist. *Sources:* ISO 27001 A.5.35,
  A.5.36; SAMM Governance.
- **GOV-05 (MUST) Exceptions recorded.** Every MUST that is not met has a recorded exception: the
  requirement, the reason, the risk, any compensating measure, who accepted the risk, and an expiry
  or review date. *Evidence:* exceptions listed in the checklist. *Sources:* ISO 27001 clause 6.1.3;
  SSDF PO.4.
- **GOV-06 (MUST) Security training.** Everyone who directs or changes the work, including external
  contributors under contract, has had security awareness training suited to the work: secure coding
  for the languages used, the handling of secrets and sensitive data, and the risks of working with
  code agents. Where the owner works alone, or no organisation provides training, recorded
  self-study meets this: a named course or guide, the date it was completed, and a refresh at least
  every two years. A code agent is "trained" by being given these documents and the repository's own
  security guidance (AGT-01). *Evidence:* training record kept by the organisation, or the owner's
  own record. *Sources:* ISO 27001 A.6.3; SSDF PO.2.2; IEC 62443-4-1 SM.
- **GOV-07 (MUST) Legal obligations recorded.** Legal and contract obligations that affect security
  are identified and recorded: for example data protection law, export control, customer security
  clauses, and product security law such as the EU Cyber Resilience Act where the software is placed
  on the EU market. For the Cyber Resilience Act this includes whether the software is in its scope
  at all (for example free and open-source software that is not supplied in the course of a
  commercial activity) and which role applies (manufacturer, or open-source software steward).
  *Evidence:* a short list in the security documentation. *Sources:* ISO 27001 A.5.31, A.5.34; EU
  CRA Article 13.
- **GOV-08 (MUST) Outsourced work bound and reviewed.** Where development is outsourced, the
  supplier is bound by contract to these requirements (or equivalent), and the delivered code is
  reviewed and tested as if it were written in-house. *Evidence:* contract clause; review records.
  *Sources:* ISO 27001 A.5.20, A.8.30.
- **GOV-09 (MUST) Public compliance record.** In a public repository, the reference to these
  requirements (GOV-03) and the filled-in checklists are published, so that compliance can be shown.
  The public checklist gives the status of each requirement and links to public evidence only. It
  MUST NOT contain: details of weaknesses that are not yet fixed (what is missing, where, or how it
  could be used), vulnerability details before the fix is released (VUL-09), names of people other
  than public maintainer handles, contact details other than the security contact, internal host
  names or network details, names of secrets, account or key identifiers, or which customers,
  programmes or organisations use the software. For a MUST that is not met, the public line says
  only "exception recorded" and the target date; the exception itself (GOV-05) is kept in a private
  record (for example a private repository, or the hosting platform's private security advisories)
  and is shown to auditors on request. *Sources:* ISO 27001 A.5.12, A.5.14, A.8.12; ISO/IEC 29147.
- **GOV-10 (MUST) No user or sector information in public repositories.** Public repositories,
  including documents, examples, test data, issue templates and agent instruction files, do not name
  customers, programmes, sectors or organisations that use the software, unless that user has agreed
  to be named in public. Only general standards are cited, never sector-specific ones, because the
  choice of sector standards shows who the users are. *Sources:* ISO 27001 A.5.12, A.8.12.
- **GOV-11 (MUST) Check before making anything public.** Everything that is made public (commits and
  their messages, merge request texts, release notes, advisories, answers to issues, checklists) is
  checked against GOV-09, GOV-10, SRC-07 and SRC-11 before it is published. For changes this check
  is part of the review (SRC-05). *Sources:* ISO 27001 A.5.14, A.8.12.

### Security Requirements and Design (DES)

- **DES-01 (MUST) Security requirements written.** The security requirements of the software are
  written down: what it protects (data and functions), against whom, and what it must not allow.
  They are derived from the classification of the data the software handles and from GOV-07.
  *Evidence:* security requirements document or section. *Sources:* ISO 27001 A.8.26; SSDF PO.1,
  PW.1; ASVS 5.0 (as a source of requirements); IEC 62443-4-1 SR; ISO/IEC 27034.
- **DES-02 (MUST) Threat model.** A threat model exists for the software: its parts, the data flows
  between them, the trust boundaries, the threats to each, and the measures against them. It MAY be
  short (one page and one diagram) for small components. *Evidence:* threat model in the repository.
  *Sources:* ISO 27001 A.8.27; SSDF PW.1.1; SAMM Design; IEC 62443-4-1 SR, SD.
- **DES-03 (MUST) Threat model reviewed on change.** The threat model and the security requirements
  are reviewed when the architecture changes, when a new external interface, data type or dependency
  of significance is added, and at least before each major release. *Evidence:* review dates.
  *Sources:* SSDF PW.2; ISO 27001 A.8.27.
- **DES-04 (MUST) Secure design principles.** The design follows secure design principles: least
  privilege, defence in depth, secure defaults, fail safe (an error denies rather than allows),
  minimal attack surface, separation of duties, and no security through obscurity. *Evidence:*
  design documentation refers to them; review records. *Sources:* ISO 27001 A.8.27; EU CRA Annex I
  Part I; ASVS 5.0 (Secure Coding and Architecture); IEC 62443-4-1 SD.
- **DES-05 (MUST) Data minimisation, data flows recorded.** The software collects, stores and sends
  only the data it needs for its purpose (data minimisation), and the design records where sensitive
  data is stored and where it is sent. *Evidence:* data flow in the threat model. *Sources:* ISO
  27001 A.5.34, A.8.12; EU CRA Annex I Part I; GDPR Article 25; ISO/IEC 27701.
- **DES-06 (SHOULD) Security functions in few places.** Security-relevant functions (authentication,
  authorisation, cryptography, parsing of untrusted input, handling of secrets) are kept in a small
  number of clearly identified places in the code, so that they can be reviewed and tested.
  *Sources:* SSDF PW.1; ASVS 5.0.
- **DES-07 (MUST) Public threat model.** In a public repository, the published threat model shows
  the threats and the measures that are in place. Threats that have no measure yet, and accepted
  risks, are kept in the private record (GOV-09) until they are addressed. *Sources:* ISO 27001
  A.5.12, A.8.27.

### Source Code and Repository (SRC)

- **SRC-01 (MUST) Everything in version control.** All source code, build scripts, CI configuration,
  infrastructure definitions and documentation are kept in version control. Nothing needed to build
  a release lives only on a personal computer. *Evidence:* a release can be built from a clean
  checkout (BLD-01). *Sources:* ISO 27001 A.8.4, A.8.9; SSDF PS.1.
- **SRC-02 (MUST) Least-privilege repository access.** Access to the repository follows least
  privilege: write access only for people who need it, admin access for as few people as possible,
  and access is removed when someone leaves the work. Where support for the application is offered
  commercially, access rights are reviewed at least once a year; otherwise access is checked when
  someone is given it or leaves the work. *Evidence:* access list and review date. *Sources:* ISO
  27001 A.5.15, A.5.18, A.8.2, A.8.4; OSPS Baseline (Access Control).
- **SRC-03 (MUST) Multi-factor authentication.** Every account with write access to the repository,
  the CI system or a package registry uses multi-factor authentication. *Evidence:* hosting platform
  setting. *Sources:* ISO 27001 A.8.5; OSPS Baseline (Access Control); SSDF PO.5.
- **SRC-04 (MUST) Protected branches.** The main branch and release branches are protected: no
  direct pushes, no force pushes, no deletion; changes arrive only through a reviewed merge request
  whose automated checks passed. Where all changes are pushed with one person's account, the
  protection requires the review check of SRC-12 instead of an approval. *Evidence:* branch
  protection settings. *Sources:* ISO 27001 A.8.4, A.8.32; SSDF PS.1; OSPS Baseline (Access
  Control); SLSA source track.
- **SRC-05 (MUST) Every change reviewed by another session or person.** Every change to a protected
  branch, whether written by a person or by a code agent, is reviewed before it is merged, by a
  reviewer other than its author: a separate code agent session or a person (README, working model).
  The review checks correctness and security, including the items in COD-01, and its result is
  recorded as SRC-12 says. A change marked as a security change is also reviewed by a person
  (CHG-02). *Evidence:* review records on merge requests. *Sources:* ISO 27001 A.8.28, A.8.32; SSDF
  PW.7; IEC 62443-4-1 SI, SVV.
- **SRC-06 (MUST) Person approves security settings.** Changes to security settings of the
  repository, the CI system or the release process (branch protection, access rights, signing keys,
  CI secrets, release workflows, agent permissions) are approved by a person, and SHOULD be approved
  by a second person. Code agents MAY propose them but never make them (AGT-05). *Evidence:*
  approval record or audit log. *Sources:* ISO 27001 A.5.3, A.8.32; IEC 62443-4-1 SM.
- **SRC-07 (MUST NOT) No secrets in repository or files.** Secrets MUST NOT be stored in the
  repository, in its history, in build or start scripts, in configuration or environment files, in
  container images, in logs or in test data. Secrets come at run time from a secret manager, an
  operating-system key store, or the CI system's protected secrets. *Evidence:* secret scanning
  (SRC-08) is clean. *Sources:* ISO 27001 A.5.17, A.8.4; SSDF PS.1; ASVS 5.0 (Configuration).
- **SRC-08 (MUST) Secret scanning.** Secret scanning runs on every push, as a check that must pass
  before a merge, and on the whole history at least once. A secret that is found is treated as
  leaked: it is revoked and replaced first, then removed from the code. Removing it from history
  alone is not enough. *Evidence:* scanner configuration and results. *Sources:* ISO 27001 A.8.12;
  SSDF PS.1; OSPS Baseline (Quality).
- **SRC-09 (SHOULD) Signed commits.** Commits to protected branches are signed, and the hosting
  platform verifies the signatures. *Sources:* SSDF PS.1, PS.2; SLSA source track.
- **SRC-10 (MUST) Changes linked to a reason.** Each change is linked to its reason: an issue, a
  requirement or a merge request description. Commit messages say what changed and why. *Evidence:*
  merge requests reference issues. *Sources:* ISO 27001 A.8.32; SSDF PS.1.
- **SRC-11 (MUST) No sensitive data in repository.** The repository holds no sensitive data: no real
  customer, personal or classified data, and no internal host names, addresses or user names that
  are not public. *Evidence:* review; scan for known patterns. *Sources:* ISO 27001 A.8.11, A.8.12,
  A.8.33.
- **SRC-12 (MUST) Review recorded as a required check.** The result of each review (SRC-05) is
  recorded on the merge request as a comment that names the reviewer (a person, or an agent session
  and its model), lists the findings and says how each was answered. It is also reported as a status
  check that branch protection requires (SRC-04). Where all changes are pushed with one person's
  account, this required check takes the place of a required approval, because the hosting platform
  does not let an account approve its own merge request. The check is set as a result of the review,
  never by the session that wrote the change. *Evidence:* review comments and check results on merge
  requests; branch protection settings. *Sources:* ISO 27001 A.8.32; SSDF PW.7; SLSA source track.
- **SRC-13 (MUST) Repository backed up.** A copy of the repository, with its full history, branches
  and tags, is kept outside the hosting platform and updated at least monthly, and restoring it is
  tried at least once a year. For an application maintained voluntarily, the copy is instead updated
  before each release, and restoring it is tried before each major release. Issues, merge requests
  and their review records SHOULD be exported as well. The copy is protected like the repository
  (SRC-02). *Evidence:* date of the last copy and of the last restore test (where the copy is kept
  goes in the private record of a public repository, GOV-09). *Sources:* ISO 27001 A.8.13; SSDF
  PS.1.
- **SRC-14 (MUST) Developer computers secured.** Computers used for the work, including those on
  which code agents run, have disk encryption on, get operating system and tool updates, lock the
  screen when unattended, and are signed in to the repository and registries only with accounts that
  use multi-factor authentication (SRC-03). Code agents on such a computer run in a sandbox or under
  a separate user account (AGT-03), not with the person's full access, and the computer holds no
  production secrets (TST-08). *Sources:* ISO 27001 A.8.1; SSDF PO.5.

### Secure Coding (COD)

- **COD-01 (MUST) Secure coding guide.** A secure coding guide for each language used is adopted (an
  existing public guide MAY be referenced) and covers at least: input validation, output encoding,
  injection (SQL, command, path, template, expression and query languages), safe deserialisation,
  safe file and path handling, integer and buffer safety where relevant, concurrency, error handling
  and resource limits. *Evidence:* guide referenced in GOV-02. *Sources:* ISO 27001 A.8.28; SSDF
  PW.5; CWE Top 25; ASVS 5.0 (Encoding and Sanitisation, Validation and Business Logic, File
  Handling); IEC 62443-4-1 SI; BSI CON.8.
- **COD-02 (MUST) Input validation.** All input from outside the trust boundary is validated against
  an allow-list of what is expected (type, length, range, format) before use. This includes files,
  network messages, command-line arguments, environment variables, configuration, database content
  written by others, and model output. *Sources:* ASVS 5.0 (Validation); CWE-20; ISO 27001 A.8.28.
- **COD-03 (MUST) Parameterised queries and commands.** Queries and commands are built with
  parameters or safe APIs, never by joining strings that contain untrusted data. Where no safe API
  exists, untrusted values are encoded for the target language. *Sources:* ASVS 5.0 (Encoding and
  Sanitisation); CWE-78, CWE-89; OWASP Top 10 A05.
- **COD-04 (MUST NOT) No execution of untrusted code.** The software MUST NOT run code, scripts or
  expressions taken from untrusted input (including dynamic class loading, `eval`, deserialisation
  of arbitrary types, and template or expression engines with access to the runtime), unless it is
  run in a sandbox designed for it. *Sources:* CWE-94, CWE-502; ASVS 5.0.
- **COD-05 (MUST) Vetted cryptography only.** Cryptography uses only well-known, maintained
  libraries and current algorithms and key sizes (for example those recommended by a national
  security agency). No home-made cryptographic algorithms or protocols. Random values for security
  use come from a cryptographically secure generator. *Sources:* ISO 27001 A.8.24; ASVS 5.0
  (Cryptography); CWE-327, CWE-338.
- **COD-06 (MUST) Safe error handling.** Errors are handled so that the software stays in a safe
  state, error messages shown to users give the reason without revealing secrets or internal
  details, and full details go to the log. *Sources:* ASVS 5.0 (Security Logging and Error
  Handling); CWE-209.
- **COD-07 (MUST NOT) No secrets in logs.** Logs, error messages, crash reports and telemetry MUST
  NOT contain secrets, and contain sensitive data only where the design (DES-05) allows it.
  *Sources:* ISO 27001 A.8.15, A.8.12; CWE-532.
- **COD-08 (MUST) Warnings as errors.** Compiler and static checker warnings are treated as errors
  for new code, or kept at zero with recorded suppressions; a suppression states why it is safe.
  *Sources:* SSDF PW.6; ISO 27001 A.8.28.
- **COD-09 (SHOULD) Memory-safe languages.** Memory-safe languages are used for new code. Where
  memory-unsafe code is used, the build enables the available hardening options (bounds checks,
  stack protection, position-independent code). *Sources:* SSDF PW.6; CISA memory safety guidance.
- **COD-10 (MUST) Bounded resource use.** Resource use triggered by input is bounded (size, depth,
  time, memory, number of items), so that a single input cannot exhaust the software. *Sources:*
  CWE-400, CWE-770; ASVS 5.0.

### Dependencies and Supply Chain (DEP)

- **DEP-01 (MUST) Trusted dependency sources.** Dependencies are obtained only from defined, trusted
  sources (for example the official package registry or an organisation's proxy repository), over
  authenticated, encrypted connections, and an internal or private group name can never be supplied
  by a public repository. Local repositories (for example a developer's local Maven repository) are
  not used in release builds. *Evidence:* repository configuration in the build. *Sources:* ISO
  27001 A.5.21; SSDF PO.3, PW.4; SLSA.
- **DEP-02 (MUST) Pinned and verified dependencies.** Dependency versions are fixed (no version
  ranges, no "latest"), and the build verifies a checksum or signature of every downloaded artefact,
  using a lock file or a dependency verification file kept in the repository. This covers build
  plug-ins, CI actions (pinned by commit hash) and container base images (pinned by digest).
  *Sources:* SSDF PW.4, PS.2; SLSA; OWASP SCVS.
- **DEP-03 (MUST) New dependencies approved.** A new direct dependency is approved before it is
  added. The check covers: need (can existing code do it?), maintenance (recent releases, more than
  one maintainer where possible), known vulnerabilities, licence (DEP-08), and its own dependencies.
  The reviewing session or person checks it. The owner, or a person the owner names, approves each
  new direct runtime dependency; a new test-only or build-only dependency MAY be approved by the
  review. *Evidence:* check and approval recorded in the merge request. *Sources:* ISO 27001 A.5.19,
  A.5.21; SSDF PW.4.1; OWASP SCVS; ISO/IEC 18974.
- **DEP-04 (MUST) Few dependencies.** The number of dependencies is kept low: unused dependencies
  are removed, and a large dependency is not added for a small function. *Sources:* SSDF PW.4; EU
  CRA Annex I Part I.
- **DEP-05 (MUST) Vulnerability scanning.** All dependencies (direct and transitive) are scanned for
  known vulnerabilities on every change, as a check that must pass before a merge, and at least
  weekly, against a public vulnerability database (for example OSV or the NVD). *Evidence:* scan
  results. *Sources:* ISO 27001 A.8.8; SSDF RV.1; EU CRA Annex I Part II.
- **DEP-06 (MUST) Dependency vulnerabilities fixed in time.** Known vulnerabilities in dependencies
  are fixed within the time limits of VUL-04 where they apply, otherwise on a best-effort basis
  (VUL-10), or have a recorded assessment that the software is not affected (for example a VEX
  statement). *Sources:* ISO 27001 A.8.8; SSDF RV.2; EU CRA Annex I Part II.
- **DEP-07 (MUST) No snapshot dependencies in releases.** Releases do not depend on unreleased or
  changeable versions of dependencies (snapshots, branches, local builds). *Sources:* SSDF PS.3;
  SLSA.
- **DEP-08 (MUST) Licences known and notices delivered.** The licences of all dependencies are known
  and compatible with how the software is used and distributed. Licence texts and notices required
  by the licences are delivered with the software. *Sources:* ISO 27001 A.5.32; ISO/IEC 5230
  (OpenChain).
- **DEP-09 (MUST) SBOM per release.** A software bill of materials (SBOM) in a standard format
  (CycloneDX or SPDX) is produced by the build for every release and kept with it. It lists all
  components with name, version, supplier, licence and a unique identifier (for example a package
  URL) and a hash. *Sources:* SSDF PS.3.2; EU CRA Annex I Part II (1); BSI TR-03183-2; OWASP SCVS.
- **DEP-10 (SHOULD) Automated dependency updates.** Dependency updates are automated (for example a
  bot that proposes update merge requests), and dependencies are kept within supported versions.
  *Sources:* SSDF RV.1; OSPS Baseline (Vulnerability Management).
- **DEP-11 (MUST) Copied code recorded.** Code copied from elsewhere (snippets, vendored files) is
  recorded with its source, version and licence, and is treated as a dependency. Agent-written code
  that reproduces a recognisable piece of existing code is treated as copied code. *Sources:* ISO
  27001 A.5.32; SSDF PW.4.
- **DEP-12 (MUST) Upstream dependencies assessed, not required to comply.** Third-party
  dependencies, including the language runtime and its standard library, are not required to meet
  these requirements: each is assessed when added (DEP-03), monitored (DEP-05) and kept up to date
  (DEP-06). The assessment is recorded, for example in the merge request that adds the dependency or
  in a dependency register. Libraries maintained by the same owner or organisation are not
  third-party: they apply the separate requirements set for libraries. *Sources:* ISO 27001 A.5.19,
  A.5.21; SSDF PW.4; EU CRA Article 13.

### Build and Release (BLD)

- **BLD-01 (MUST) Scripted build.** The build is fully scripted and runs from a clean checkout with
  one documented command, without manual steps. *Sources:* SSDF PO.3, PS.3; SLSA Build L1.
- **BLD-02 (MUST) Releases built in CI.** Releases are built by the CI system on a hosted or managed
  build platform, not on a personal computer. *Sources:* SLSA Build L2; SSDF PO.5.
- **BLD-03 (MUST) Build environment defined.** The build environment is defined in the repository
  (tool versions, base images) and kept up to date. *Sources:* SSDF PO.3, PO.5; ISO 27001 A.8.9.
- **BLD-04 (MUST) Least-privilege CI.** CI jobs run with the least privileges they need: tokens are
  read-only by default, write and publishing rights are given only to the release job, and secrets
  are not available to jobs started from untrusted contributions (for example merge requests from
  forks). Values that others can set (branch names, tags, commit messages, merge request titles and
  descriptions, author names) are quoted or validated before a pipeline uses them, and are never put
  directly into a shell command. *Sources:* SSDF PO.5; OSPS Baseline (Build and Release).
- **BLD-05 (MUST) Versioned, traceable releases.** Each release has a unique version number, and the
  release is traceable to the exact source commit it was built from (for example a signed tag).
  *Sources:* ISO 27001 A.8.32; SSDF PS.3; SLSA.
- **BLD-06 (MUST) Signed artefacts with checksums.** Release artefacts are signed, and published
  with checksums, so that users can check that what they received is what was built. Signing keys
  are kept in a key store or the CI system's protected secrets, never in the repository, and their
  use is logged. *Sources:* SSDF PS.2; ISO 27001 A.8.24; EU CRA Annex I Part I; SLSA; IEC 62443-4-1
  SUM.
- **BLD-07 (SHOULD) Build provenance.** The build produces provenance (a signed record of what was
  built, from which source, by which build) in the SLSA format. *Sources:* SLSA Build L2/L3; SSDF
  PS.3.2.
- **BLD-08 (SHOULD) Reproducible builds.** Builds are reproducible: building the same commit twice
  gives the same artefacts. *Sources:* SSDF PW.6; SLSA.
- **BLD-09 (MUST) Person approves releases.** A release is approved by a person (the owner or
  deputy) after the release checks (TST-07) pass. Code agents MAY prepare a release but MUST NOT
  approve or publish it. A second person SHOULD approve releases given to anyone outside the
  development team (README, working model). *Sources:* ISO 27001 A.8.29, A.8.32; SSDF PO.4.
- **BLD-10 (MUST) Release notes and change log.** Each release has release notes (a change log) that
  list new features, changed behaviour, removed features, fixed faults, and security fixes with
  their identifiers (for example CVE ids) where they exist. *Sources:* EU CRA Annex I Part II; SSDF
  RV.2; ISO 9001 8.5.6.
- **BLD-11 (MUST) Releases archived.** Releases, their SBOMs, provenance, build logs, test results,
  review records and release decisions are archived for the support period of the release (VUL-07),
  so that any release can be examined later. *Sources:* SSDF PS.3; ISO 27001 A.5.33; ISO 9001 7.5.3.
- **BLD-12 (MUST NOT) No debug features in releases.** Debug features, test accounts, test keys and
  development settings MUST NOT be enabled in releases. *Sources:* ISO 27001 A.8.31; ASVS 5.0
  (Configuration).
- **BLD-13 (MUST) Pre-releases.** A pre-release (README, terms) is built by CI (BLD-02), or by the
  scripted build (BLD-01) from a clean checkout of a tagged commit. Its name and its version
  information mark it as a pre-release, it comes with an SBOM (DEP-09) and checksums, and a record
  says which commit it was built from and who received it (kept in the private record of a public
  repository, GOV-09). The owner approves who receives it. BLD-06, BLD-07, BLD-10, BLD-11, TST-07
  and QRI-01 do not apply to pre-releases. A pre-release is not used in production and is not given
  beyond the named group; a build that is, is a release. *Sources:* ISO 27001 A.8.32; SSDF PS.3.

### Verification and Testing (TST)

- **TST-01 (MUST) Automated tests block merges.** Automated tests run in CI on every change, and a
  change is not merged while tests fail. Tests are not removed, skipped or weakened to make a change
  pass; a test that is wrong is fixed in a reviewed change with the reason recorded. A test that
  fails at random is quarantined only as QCR-04 allows. *Sources:* ISO 27001 A.8.29; SSDF PW.8.
- **TST-02 (MUST) Security requirements tested.** Each security requirement (DES-01) and each
  measure in the threat model (DES-02) that can be tested has a test, including negative tests (what
  must be refused). *Sources:* ISO 27001 A.8.29; SSDF PW.8; ASVS 5.0; IEC 62443-4-1 SVV.
- **TST-03 (MUST) Static analysis.** Static analysis for security (SAST) runs on every change, with
  rules for the languages used. New findings of high severity block the merge until fixed or
  assessed. *Sources:* SSDF PW.7, PW.8; ISO 27001 A.8.28, A.8.29; IEC 62443-4-1 SVV.
- **TST-04 (retired in 0.3).** Merged into DEP-05 and SRC-08.
- **TST-05 (SHOULD) Fuzz testing of parsers.** Code that parses untrusted or complex input (file
  formats, network protocols, languages) is fuzz tested. *Sources:* SSDF PW.8; OpenSSF Scorecard
  (Fuzzing); IEC 62443-4-1 SVV.
- **TST-06 (MUST) No real sensitive test data.** Test data contains no real sensitive data. Where
  real data is unavoidable, its use is approved by its owner, it is protected as in production, and
  it is deleted after the test. *Sources:* ISO 27001 A.8.33.
- **TST-07 (MUST) Release checks recorded.** Before a release, the release checks are run and
  recorded: all tests pass, no open findings of high or critical severity without an exception, the
  SBOM is produced, and the checklists are up to date. *Sources:* ISO 27001 A.8.29; SSDF PO.4.
- **TST-08 (MUST) Separate environments.** Development, test and production environments are
  separate. Development and test do not use production secrets or production data, and production is
  not changed from a developer's computer. *Sources:* ISO 27001 A.8.31.
- **TST-09 (SHOULD) Coverage measured.** Test coverage is measured, and security-relevant code
  (DES-06) has high coverage. *Sources:* SSDF PW.8.

### Change Management (CHG)

- **CHG-01 (retired in 0.3).** Merged into GOV-02 and SRC-05.
- **CHG-02 (MUST) Security changes marked and checked.** A change that affects security (a trust
  boundary, authentication, authorisation, cryptography, secrets, data flows, dependencies, the
  build or the release process) is marked as such, its review checks it against the threat model,
  and it is also reviewed by a person before it is merged. *Sources:* ISO 27001 A.8.32; SSDF PW.2.
- **CHG-03 (MUST) Emergency changes reviewed afterwards.** Emergency changes (for example an urgent
  security fix) MAY be merged once the automated checks and the review check (SRC-12) have passed,
  before the person review that CHG-02 asks for. The person review follows before the next release,
  or within five working days where support for the application is offered commercially, and the
  reason is recorded. *Sources:* ISO 27001 A.8.32.

### Vulnerability Management and Incidents (VUL)

- **VUL-01 (MUST) Security policy.** The repository has a security policy (`SECURITY.md`) that says
  how to report a vulnerability privately, who receives reports, what response to expect (VUL-10),
  and which versions get security fixes. The reporting channel is a dedicated security address or
  the hosting platform's private vulnerability reporting, not a personal address. *Sources:* EU CRA
  Annex I Part II (5, 6); ISO/IEC 29147; OSPS Baseline (Vulnerability Management); SSDF RV.1.3; IEC
  62443-4-1 DM.
- **VUL-02 (MUST) Reports acknowledged and assessed.** A vulnerability report is acknowledged and is
  assessed for severity (for example with CVSS) and for whether it is exploitable in the software.
  Where support for the application is offered commercially, the report is acknowledged within five
  working days; otherwise there is no time limit (VUL-10). *Sources:* ISO/IEC 30111; SSDF RV.2.1;
  IEC 62443-4-1 DM.
- **VUL-03 (MUST) Vulnerabilities tracked.** Vulnerabilities, found in the code or in dependencies,
  are tracked in one place until closed, with their severity, status and the release that fixes
  them. *Sources:* ISO 27001 A.8.8; SSDF RV.2; IEC 62443-4-1 DM.
- **VUL-04 (SHOULD) Fix time limits.** This is a MUST where support for the application is offered
  commercially; an application maintained voluntarily states instead that it has no guaranteed times
  (VUL-10). Vulnerabilities are dealt with within these limits from the time they are known, unless
  an exception (GOV-05) is recorded. Critical: a mitigation, or a security advisory with a
  workaround, within 7 days, and a fixed release within 30 days. High: a fixed release within 30
  days. Medium: within 90 days. Low: at the next planned release. Actively exploited vulnerabilities
  are mitigated, or users are warned, at once. These limits are the choice of these documents (the
  EU CRA asks for "without delay"); the organisation MAY set shorter limits, and the limits that
  apply are stated in `SECURITY.md` (VUL-01). *Sources:* ISO 27001 A.8.8; EU CRA Annex I Part II
  (2).
- **VUL-05 (MUST) Security advisories.** Users are told about fixed vulnerabilities: a security
  advisory with the affected versions, the fixed version, the severity and what users should do.
  Where the software is placed on the EU market, the reporting duties of the EU Cyber Resilience Act
  are followed: actively exploited vulnerabilities and severe incidents are reported as its Article
  14 requires (these duties apply from 11 September 2026). *Sources:* EU CRA Article 14, Annex I
  Part II (4); ISO/IEC 29147.
- **VUL-06 (MUST) Root cause analysis.** For each vulnerability of high or critical severity, the
  root cause is found, and the process, tests or checks are changed so that the same kind of fault
  is caught in future. *Sources:* SSDF RV.3; ISO 27001 A.5.27; IEC 62443-4-1 DM.
- **VUL-07 (MUST) Support period stated.** The support period during which security fixes are given
  is stated for each release, and users are told in advance when support ends. Where the EU CRA
  applies, the support period is at least five years, unless the software is expected to be in use
  for a shorter time (Article 13). *Sources:* EU CRA Article 13, Annex II; SSDF RV.
- **VUL-08 (MUST) Development incidents reported.** A security incident in the development
  environment (for example a leaked secret, a compromised account, a tampered dependency or build)
  is reported to the organisation's incident process at once, and affected releases are identified.
  *Sources:* ISO 27001 A.5.24 to A.5.28.
- **VUL-09 (MUST) Coordinated disclosure.** Details of a vulnerability are not made public (in
  issues, commits, merge request texts, release notes or the checklist) until a fixed release is
  available, or until the disclosure date agreed with the reporter. Fixes for vulnerabilities that
  are not yet public are prepared in a private workspace (for example the hosting platform's private
  advisory fork), and the public commit message does not describe how to exploit the fault.
  *Sources:* ISO/IEC 29147, 30111; EU CRA Annex I Part II; SSDF RV.2.
- **VUL-10 (MUST) Response expectations stated.** The security policy (VUL-01) states honestly what
  users can expect. An application maintained voluntarily says that reports are handled on a
  best-effort basis and that no response or fix time is guaranteed. Where support is offered
  commercially, the policy states the times of VUL-02 and VUL-04. *Sources:* ISO/IEC 29147; OSPS
  Baseline (Vulnerability Management).

### Delivered Software and Documentation (PRD)

- **PRD-01 (MUST) Secure defaults.** The software is delivered with a secure default configuration:
  no default or shared passwords, no unneeded network services, encryption on by default, least
  privilege for its own processes. *Sources:* EU CRA Annex I Part I; ASVS 5.0 (Configuration); SSDF
  PW.9.
- **PRD-02 (MUST) Security documentation for users.** The software is delivered with security
  documentation for its users and administrators: what it does with data, which connections it
  makes, what it installs or changes, how to configure it securely, how to update it, and how to
  remove it and its data. *Sources:* EU CRA Annex II; ISO 27001 A.5.37; IEC 62443-4-1 SG.
- **PRD-03 (MUST) Updates keep user data.** Security updates can be installed without loss of user
  data or configuration, and the documentation says how. *Sources:* EU CRA Annex I Part I; IEC
  62443-4-1 SUM.
- **PRD-04 (SHOULD) Complete removal.** The software can be removed completely, including its stored
  data, and the documentation says how. *Sources:* EU CRA Annex I Part I; ISO 27001 A.8.10.

## Checklist

Status: **met**, **partly**, **not met**, **n/a**. Every "not met" MUST and every "n/a" needs a
short reason; a "not met" MUST also needs an exception (GOV-05). In a public repository, the
evidence column follows GOV-09: status, public links and target dates only.

| Id | Level | Requirement | Status | Evidence or reason |
|----|-------|-------------|--------|--------------------|
| GOV-01 | MUST | Named owner (a person) | | |
| GOV-02 | MUST | Process written down | | |
| GOV-03 | MUST | Applicable documents recorded | | |
| GOV-04 | MUST | Checklist reviewed yearly and before major releases | | |
| GOV-05 | MUST | Exceptions recorded | | |
| GOV-06 | MUST | Security training | | |
| GOV-07 | MUST | Legal obligations recorded | | |
| GOV-08 | MUST | Outsourced work bound and reviewed | | |
| GOV-09 | MUST | Public compliance record | | |
| GOV-10 | MUST | No user or sector information in public repositories | | |
| GOV-11 | MUST | Check before making anything public | | |
| DES-01 | MUST | Security requirements written | | |
| DES-02 | MUST | Threat model | | |
| DES-03 | MUST | Threat model reviewed on change | | |
| DES-04 | MUST | Secure design principles | | |
| DES-05 | MUST | Data minimisation, data flows recorded | | |
| DES-06 | SHOULD | Security functions in few places | | |
| DES-07 | MUST | Public threat model | | |
| SRC-01 | MUST | Everything in version control | | |
| SRC-02 | MUST | Least-privilege repository access | | |
| SRC-03 | MUST | Multi-factor authentication | | |
| SRC-04 | MUST | Protected branches | | |
| SRC-05 | MUST | Every change reviewed by another session or person | | |
| SRC-06 | MUST | Person approves security settings | | |
| SRC-07 | MUST NOT | No secrets in repository or files | | |
| SRC-08 | MUST | Secret scanning | | |
| SRC-09 | SHOULD | Signed commits | | |
| SRC-10 | MUST | Changes linked to a reason | | |
| SRC-11 | MUST | No sensitive data in repository | | |
| SRC-12 | MUST | Review recorded as a required check | | |
| SRC-13 | MUST | Repository backed up | | |
| SRC-14 | MUST | Developer computers secured | | |
| COD-01 | MUST | Secure coding guide | | |
| COD-02 | MUST | Input validation | | |
| COD-03 | MUST | Parameterised queries and commands | | |
| COD-04 | MUST NOT | No execution of untrusted code | | |
| COD-05 | MUST | Vetted cryptography only | | |
| COD-06 | MUST | Safe error handling | | |
| COD-07 | MUST NOT | No secrets in logs | | |
| COD-08 | MUST | Warnings as errors | | |
| COD-09 | SHOULD | Memory-safe languages | | |
| COD-10 | MUST | Bounded resource use | | |
| DEP-01 | MUST | Trusted dependency sources | | |
| DEP-02 | MUST | Pinned and verified dependencies | | |
| DEP-03 | MUST | New dependencies approved | | |
| DEP-04 | MUST | Few dependencies | | |
| DEP-05 | MUST | Vulnerability scanning | | |
| DEP-06 | MUST | Dependency vulnerabilities fixed in time | | |
| DEP-07 | MUST | No snapshot dependencies in releases | | |
| DEP-08 | MUST | Licences known and notices delivered | | |
| DEP-09 | MUST | SBOM per release | | |
| DEP-10 | SHOULD | Automated dependency updates | | |
| DEP-11 | MUST | Copied code recorded | | |
| DEP-12 | MUST | Upstream dependencies assessed, not required to comply | | |
| BLD-01 | MUST | Scripted build | | |
| BLD-02 | MUST | Releases built in CI | | |
| BLD-03 | MUST | Build environment defined | | |
| BLD-04 | MUST | Least-privilege CI | | |
| BLD-05 | MUST | Versioned, traceable releases | | |
| BLD-06 | MUST | Signed artefacts with checksums | | |
| BLD-07 | SHOULD | Build provenance | | |
| BLD-08 | SHOULD | Reproducible builds | | |
| BLD-09 | MUST | Person approves releases | | |
| BLD-10 | MUST | Release notes and change log | | |
| BLD-11 | MUST | Releases archived | | |
| BLD-12 | MUST NOT | No debug features in releases | | |
| BLD-13 | MUST | Pre-releases | | |
| TST-01 | MUST | Automated tests block merges | | |
| TST-02 | MUST | Security requirements tested | | |
| TST-03 | MUST | Static analysis | | |
| TST-05 | SHOULD | Fuzz testing of parsers | | |
| TST-06 | MUST | No real sensitive test data | | |
| TST-07 | MUST | Release checks recorded | | |
| TST-08 | MUST | Separate environments | | |
| TST-09 | SHOULD | Coverage measured | | |
| CHG-02 | MUST | Security changes marked and checked | | |
| CHG-03 | MUST | Emergency changes reviewed afterwards | | |
| VUL-01 | MUST | Security policy | | |
| VUL-02 | MUST | Reports acknowledged and assessed | | |
| VUL-03 | MUST | Vulnerabilities tracked | | |
| VUL-04 | SHOULD | Fix time limits | | |
| VUL-05 | MUST | Security advisories | | |
| VUL-06 | MUST | Root cause analysis | | |
| VUL-07 | MUST | Support period stated | | |
| VUL-08 | MUST | Development incidents reported | | |
| VUL-09 | MUST | Coordinated disclosure | | |
| VUL-10 | MUST | Response expectations stated | | |
| PRD-01 | MUST | Secure defaults | | |
| PRD-02 | MUST | Security documentation for users | | |
| PRD-03 | MUST | Updates keep user data | | |
| PRD-04 | SHOULD | Complete removal | | |
