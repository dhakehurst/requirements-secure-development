# 05 Applications and Services

Part of the Secure Development Requirements for Applications, version 0.6 (draft), 2026-11-25. Read
the [README](README.md) first: it gives the wording rules, the working model, the terms and the
sources.

## Scope

Applies, with documents 01 to 03, to every repository in this set: it delivers software that people
run: a desktop or mobile application, a command-line tool, a server or a web service. Any
application MAY follow the one-person profile below.

## One-Person Profile

Any application MAY follow the one-person profile, whatever the number of people who take part, so
that one person working with code agents is always enough to meet the requirements, and nothing more
is asked of volunteers. It is used instead of all of documents 01 to 03, 05, 06 and 07. Under this
profile, the requirements listed below stay as they are, and every other MUST of those documents
counts as SHOULD. The choice is recorded (GOV-03). Requirements of documents 06 and 07 in the list
apply only where those documents apply.

The profile keeps what protects users and the repository most: control of the repository and of
releases, review of every change and person review of security changes, no secrets, the main secure
coding rules, verified and scanned dependencies, signed releases with an SBOM, vulnerability
handling, secure defaults, the rules for code agents and for public repositories, and the main rules
for software that uses language models. Requirements that need a second person, paid services or a
large ongoing documentation effort are SHOULD under this profile; in particular code signing of
installers (APP-08, KMP-22) is a SHOULD, because it needs paid certificates.

A SHOULD that is not met needs a short recorded reason (README, section 3).

| Id | Level | Requirement | Document | Status | Evidence or reason |
|----|-------|-------------|----------|--------|--------------------|
| GOV-01 | MUST | Named owner (a person) | 01 | | |
| GOV-03 | MUST | Applicable documents recorded | 01 | | |
| GOV-05 | MUST | Exceptions recorded | 01 | | |
| GOV-09 | MUST | Public compliance record | 01 | | |
| GOV-10 | MUST | No user or sector information in public repositories | 01 | | |
| GOV-11 | MUST | Check before making anything public | 01 | | |
| DES-02 | MUST | Threat model | 01 | | |
| DES-05 | MUST | Data minimisation, data flows recorded | 01 | | |
| SRC-02 | MUST | Least-privilege repository access | 01 | | |
| SRC-03 | MUST | Multi-factor authentication | 01 | | |
| SRC-04 | MUST | Protected branches | 01 | | |
| SRC-05 | MUST | Every change reviewed by another session or person | 01 | | |
| SRC-06 | MUST | Person approves security settings | 01 | | |
| SRC-07 | MUST NOT | No secrets in repository or files | 01 | | |
| SRC-08 | MUST | Secret scanning | 01 | | |
| SRC-12 | MUST | Review recorded as a required check | 01 | | |
| SRC-14 | MUST | Developer computers secured | 01 | | |
| COD-02 | MUST | Input validation | 01 | | |
| COD-03 | MUST | Parameterised queries and commands | 01 | | |
| COD-04 | MUST NOT | No execution of untrusted code | 01 | | |
| COD-05 | MUST | Vetted cryptography only | 01 | | |
| COD-07 | MUST NOT | No secrets in logs | 01 | | |
| DEP-01 | MUST | Trusted dependency sources | 01 | | |
| DEP-02 | MUST | Pinned and verified dependencies | 01 | | |
| DEP-03 | MUST | New dependencies approved | 01 | | |
| DEP-05 | MUST | Vulnerability scanning | 01 | | |
| DEP-06 | MUST | Dependency vulnerabilities fixed in time | 01 | | |
| DEP-08 | MUST | Licences known and notices delivered | 01 | | |
| DEP-09 | MUST | SBOM per release | 01 | | |
| BLD-02 | MUST | Releases built in CI | 01 | | |
| BLD-04 | MUST | Least-privilege CI | 01 | | |
| BLD-06 | MUST | Signed artefacts with checksums | 01 | | |
| BLD-09 | MUST | Person approves releases | 01 | | |
| BLD-12 | MUST NOT | No debug features in releases | 01 | | |
| BLD-13 | MUST | Pre-releases | 01 | | |
| TST-01 | MUST | Automated tests block merges | 01 | | |
| CHG-02 | MUST | Security changes marked and checked | 01 | | |
| VUL-01 | MUST | Security policy | 01 | | |
| VUL-02 | MUST | Reports acknowledged and assessed | 01 | | |
| VUL-10 | MUST | Response expectations stated | 01 | | |
| VUL-05 | MUST | Security advisories | 01 | | |
| VUL-09 | MUST | Coordinated disclosure | 01 | | |
| PRD-01 | MUST | Secure defaults | 01 | | |
| PRD-02 | MUST | Security documentation for users | 01 | | |
| APP-03 | MUST | Authorisation, source rights kept | 05 | | |
| APP-04 | MUST | TLS and listening interfaces | 05 | | |
| APP-05 | MUST | Secrets at run time only | 05 | | |
| AGT-03 | MUST | Agents sandboxed, least privilege | 02 | | |
| AGT-05 | MUST NOT | No changes to protected settings or releases | 02 | | |
| AGT-06 | MUST NOT | No weakening of checks | 02 | | |
| AGT-08 | MUST | Read content is data, not instructions | 02 | | |
| AGT-14 | MUST | Stop and ask before irreversible steps | 02 | | |
| AGT-18 | MUST | Agents keep private context out of public text | 02 | | |
| AGT-19 | MUST | Agent extensions vetted | 02 | | |
| AGT-20 | MUST | Owner samples agent reviews | 02 | | |
| AI-02 | MUST | External content untrusted (prompt injection) | 06 | | |
| AI-03 | MUST | Model output validated | 06 | | |
| AI-06 | MUST | Data sent only to approved models | 06 | | |
| AI-07 | MUST NOT | No secrets in prompts | 06 | | |
| TQS-01 | MUST | Intended use and status stated | 07 | | |
| TQS-10 | MUST | Invalid input reported | 07 | | |

## Requirements

- **APP-01 (MUST) ASVS level chosen and checked.** The application has a chosen verification level
  of the OWASP Application Security Verification Standard (ASVS) 5.0: Level 1 at least, Level 2 for
  software that handles sensitive data or is reachable over a network by more than one user. For a
  desktop or command-line application without a web interface, the chapters that normally apply are
  Encoding and Sanitisation, Validation and Business Logic, File Handling, Cryptography, Secure
  Communication, Configuration, Data Protection, Secure Coding and Architecture, and Security
  Logging and Error Handling; the others are recorded as n/a with a reason. The applicable chapters
  are checked before each major release and the result is recorded. *Sources:* ASVS 5.0; ISO 27001
  A.8.26, A.8.29; ISO/IEC 27034.
- **APP-02 (MUST) Authentication.** Users are authenticated with the organisation's identity system
  where one exists, rather than with passwords stored by the application. Where the application
  stores passwords, they are stored with a current password hashing function (for example Argon2id,
  scrypt or PBKDF2 with a high work factor). *Sources:* ASVS 5.0 (Authentication); ISO 27001 A.5.17,
  A.8.5.
- **APP-03 (MUST) Authorisation, source rights kept.** Every access to data or functions is
  authorised on the server side (or in the trusted part of the software), by default denying access.
  Where the application shows data from other systems, it does not give users access to data they
  could not see in the source system, unless this is a documented and approved design decision.
  *Sources:* ASVS 5.0 (Authorisation); OWASP Top 10 A01; ISO 27001 A.5.15, A.8.3.
- **APP-04 (MUST) TLS and listening interfaces.** Network connections use TLS 1.2 or later with
  certificate validation; certificate validation is never turned off, including in tests against
  production-like systems. Services listen only on the interfaces they need (local services only on
  the loopback interface). *Sources:* ASVS 5.0 (Secure Communication); ISO 27001 A.8.20, A.8.21,
  A.8.24.
- **APP-05 (MUST) Secrets at run time only.** The application obtains secrets at run time from a
  secret manager or an operating-system key store, keeps them in memory no longer than needed, and
  never writes them into its configuration, project files, exports or logs. *Sources:* SRC-07; ASVS
  5.0 (Configuration, Data Protection); ISO 27001 A.5.17.
- **APP-06 (MUST) Sensitive data protected at rest.** Sensitive data stored by the application is
  protected at rest (encryption or operating-system file protection, as the classification requires)
  and is stored only where the design says (DES-05). *Sources:* ASVS 5.0 (Data Protection); ISO
  27001 A.8.24, A.8.12.
- **APP-07 (MUST) Security event logging.** Where the application has user accounts, sign-in or
  rights, security-relevant events are logged: sign-in and sign-in failures, access denied, changes
  to configuration and rights, and errors in security functions, with time, user and outcome. Logs
  are protected from change and kept for a defined period. A single-user application without sign-in
  logs errors in security functions and changes to its security configuration. *Sources:* ASVS 5.0
  (Security Logging and Error Handling); ISO 27001 A.8.15; OWASP Top 10 A09.
- **APP-08 (MUST) Code signing.** Installers and executables are code-signed with a certificate
  trusted by the target platforms. *Sources:* SSDF PS.2; EU CRA Annex I Part I.
- **APP-09 (MUST) External programs, connections and writes stated.** The application states every
  external program it starts, every network connection it makes and every location it writes to
  (PRD-02), and does none of these with input that has not been validated. *Sources:* ISO 27001
  A.8.26; COD-03, COD-04.
- **APP-10 (MUST) Hardened containers and deployments.** Container images and server deployments run
  as a non-root user, with a read-only file system where possible, and only the ports they need.
  Images are built from pinned, maintained base images and scanned (DEP-05). *Sources:* ISO 27001
  A.8.9; SSDF PW.9.
- **APP-11 (SHOULD) Penetration test.** A penetration test or an independent security review is done
  before the first release to a wider group of users and after major changes to the architecture.
  *Sources:* ISO 27001 A.8.29; SAMM Verification.
- **APP-12 (SHOULD) Web security headers.** Web interfaces use the browser security headers that
  apply (content security policy, frame protection, strict transport security) and protect against
  cross-site request forgery. *Sources:* ASVS 5.0 (Web Frontend Security); OWASP Top 10.

## Checklist

Status: **met**, **partly**, **not met**, **n/a**. Every "not met" MUST and every "n/a" needs a
short reason; a "not met" MUST also needs an exception (GOV-05). In a public repository, the
evidence column follows GOV-09: status, public links and target dates only.

| Id | Level | Requirement | Status | Evidence or reason |
|----|-------|-------------|--------|--------------------|
| APP-01 | MUST | ASVS level chosen and checked | | |
| APP-02 | MUST | Authentication | | |
| APP-03 | MUST | Authorisation, source rights kept | | |
| APP-04 | MUST | TLS and listening interfaces | | |
| APP-05 | MUST | Secrets at run time only | | |
| APP-06 | MUST | Sensitive data protected at rest | | |
| APP-07 | MUST | Security event logging | | |
| APP-08 | MUST | Code signing | | |
| APP-09 | MUST | External programs, connections and writes stated | | |
| APP-10 | MUST | Hardened containers and deployments | | |
| APP-11 | SHOULD | Penetration test | | |
| APP-12 | SHOULD | Web security headers | | |
