# Secure Development Requirements for Applications

Version 0.4 (draft), 2026-11-25

## 1. Purpose

This set of documents gives the requirements that a software development MUST meet so that its
process, and the software it delivers, meet common security and quality standards. It is generic: it
applies to any repository, whatever the product or the organisation.

This set is for repositories that deliver software that people run: desktop or mobile applications,
command-line tools, servers and web services. Libraries use the separate set for libraries.

It is written for the people in charge of a repository and for the code agents that work in it. A
code agent given these documents applies them to the repository it works in, and reports which
requirements are met, which are not, and why.

The requirements are mostly about the development process. The software is the end result of that
process, so some requirements are about the software itself.

## 2. The Documents

| Document | Applies | Ids |
|----------|---------|-----|
| [01 Core secure development](01-core-secure-development.md) | always | GOV, DES, SRC, COD, DEP, BLD, TST, CHG, VUL, PRD |
| [02 Development by AI code agents](02-ai-code-agents.md) | always (development is done mainly by code agents) | AGT |
| [03 Quality](03-quality.md) | always | QPL, QCM, QCR, QDO, QRI |
| [05 Applications and services](05-applications-and-services.md) | always (includes the one-person profile) | APP |
| [06 Software that uses LLMs](06-llm-software.md) | the software sends data to a language model, uses retrieval, or lets a model call tools | AI |
| [07 Tool qualification support](07-tool-qualification-support.md) | the application may be used to develop or verify safety-related systems | TQS |
| [A1 Kotlin Multiplatform annex](A1-kotlin-multiplatform-annex.md) | the repository uses Kotlin Multiplatform and Gradle | KMP |
| [Adoption guide](adoption-guide.md) | the repository existed before these requirements were applied | (none) |

An application's own libraries (maintained by the same owner) follow the set for libraries.
Third-party dependencies, including the language runtime and its standard library, are assessed and
monitored but are not required to meet these requirements (DEP-12). Any application MAY follow the
**one-person profile** in document 05 instead of the full set, so that one person working with code
agents is always enough.

Each requirements document ends with its own checklist. A repository copies the checklists of the
documents that apply to it into one file and fills them in (GOV-03).

## 3. Requirement Wording

The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY are used as in RFC 2119 and RFC 8174 (they
have this meaning only when written in capitals).

- **MUST / MUST NOT**: required. Not meeting it needs a recorded exception (GOV-05).
- **SHOULD / SHOULD NOT**: expected. Not meeting it needs a short recorded reason.
- **MAY**: optional good practice.

Each requirement has an id, a level, a short title, the requirement, often the **evidence** that
shows it is met, and the **sources** it comes from (section 8). Ids are stable across versions: a
requirement that is removed keeps its id unused, so that checklists stay comparable.

Where these requirements and an organisation's own policy differ, the stricter one applies.

## 4. Working Model

Development is assumed to be done mainly by code agents, directed by people:

1. **A person asks for the work** and stays responsible for it. The owner of the repository is
   always a person.
2. **A code agent session writes the change** in its own sandbox, with credentials limited to the
   task, following these requirements.
3. **A separate code agent session reviews the change.** It is given the change, its reason and
   these requirements, not the reasoning of the session that wrote it. A person MAY review instead
   or as well. A session never reviews its own change. The result is recorded as a required check
   (SRC-12). A change marked as a security change (CHG-02) is reviewed by a person as well, and the
   owner reviews a sample of agent-reviewed changes each month (AGT-20).
4. **A person approves** anything that changes security settings of the repository, CI or release
   process (SRC-06), every release (BLD-09), every exception (GOV-05), and any step that cannot be
   undone (AGT-14).

Where these documents ask for a "review", a review by a separate agent session meets it, provided
the review and its result are recorded. Where they ask for a "person", an agent does not meet it.
Where they ask for a "second person" and only one person works on the repository, or the one-person
profile is used: for a MUST, the owner records an exception (GOV-05) and reviews the change
themselves at a later time, separate from the change, with a recorded result; for a SHOULD, a short
recorded reason is enough.

## 5. Public Repositories

These requirements and each repository's filled-in checklists are meant to be published in the
repository, so that anyone can see that it complies. Publishing them must not weaken the security it
shows. The rules for that are GOV-09 to GOV-11, DES-07, VUL-09 and AGT-18; in short:

- **Public**: the requirements, which of them apply, the status of each, links to public evidence
  (CI results, published SBOMs, signatures, `SECURITY.md`), target dates for open items.
- **Private**: details of open gaps and exceptions, threats without a measure yet, vulnerabilities
  before their fix is released, names and contacts of people beyond public handles, internal
  systems, and who uses the software. The private record is shown to auditors on request.
- **Not named in public**: customers, programmes, sectors or organisations that use the software.
  That is why these documents cite only general standards, never sector-specific ones.

Where a repository is first brought into line (adoption guide), it SHOULD complete the quick wins
before it first publishes its checklist, so that the public record starts with few open items.

## 6. Terms

- **Repository**: the version-controlled source of one product or component, with its build and
  release configuration.
- **Owner**: the person accountable for the repository (GOV-01).
- **Code agent**: an AI assistant that reads, writes, builds, tests or commits code. An **agent
  session** is one run of a code agent with its own context and workspace.
- **Agent extension**: an MCP server, plug-in, skill, hook or other component that adds tools,
  instructions or automatic actions to a code agent.
- **Release**: any build that is given to anyone outside the development team, including test users,
  other than a pre-release.
- **Pre-release**: a build given to a small, named group of test users for evaluation (for example a
  demonstration build), marked as a pre-release. Pre-releases follow BLD-13 instead of the full
  release requirements.
- **Dependency**: any third-party component used to build, test or run the software, including build
  plug-ins, CI actions, container base images and AI models.
- **Secret**: a password, token, private key, API key or other credential.
- **Sensitive data**: personal data, customer or partner data, export-controlled data, and any data
  classified above "public" by the organisation that owns it.

## 7. Principles

These principles explain the requirements. Where a situation is not covered, apply the principle.

1. **Security and quality are part of every step**, not a separate phase at the end.
2. **Least privilege**: people, tools, agents and the software itself get only the access they need,
   for only as long as they need it.
3. **Secure by default**: the software is safe when installed and run with its default settings.
4. **Trust nothing from outside**: input, dependencies, downloaded files, model output and content
   read by agents are all untrusted until checked.
5. **Everything is traceable**: every change, build and release can be traced to who asked for it,
   who or what made it, why, and from which source.
6. **Automate checks**: a check that runs on every change is worth more than one done by hand.
7. **People decide**: agents do the work; people approve risks, releases and anything that cannot be
   undone.
8. **Record decisions**: risks that are accepted are written down with a reason and an owner.

## 8. Sources

The requirements are derived from these public standards and guides. Where a source is a management
system standard (ISO 27001, ISO 9001), the requirements here are one way of meeting its controls for
software development; they do not replace the organisation's own policies.

### Security

| Short name | Source |
|------------|--------|
| ISO 27001 | ISO/IEC 27001:2022, Information security management systems, Annex A (mainly A.5.8, A.5.19 to A.5.23, A.8.1, A.8.4, A.8.8, A.8.9, A.8.13, A.8.24 to A.8.34) |
| ISO 27002 | ISO/IEC 27002:2022, guidance for the ISO 27001 Annex A controls |
| ISO/IEC 27034 | Application security |
| ISO/IEC 27701 | Privacy information management |
| ISO/IEC 29147, 30111 | Vulnerability disclosure; vulnerability handling processes |
| ISO/IEC 5230, 18974 | OpenChain licence compliance; OpenChain security assurance |
| IEC 62443-4-1 | Secure product development life cycle requirements (practices SM security management, SR security requirements, SD secure by design, SI secure implementation, SVV security verification and validation testing, DM defect management, SUM security update management, SG security guidelines) |
| SSDF | NIST SP 800-218, Secure Software Development Framework 1.1 (practices PO, PS, PW, RV). Version 1.2 (SP 800-218 Rev. 1) was still a draft when this version was written; its practice ids may differ |
| BSI TR-03185 | German Federal Office for Information Security, Technical Guideline Secure Software Lifecycle |
| BSI TR-03183-2 | German Federal Office for Information Security, Technical Guideline on SBOMs |
| BSI CON.8 | BSI IT-Grundschutz module CON.8, Software development |
| SAMM | OWASP Software Assurance Maturity Model 2 |
| ASVS 5.0 | OWASP Application Security Verification Standard 5.0 |
| OWASP Top 10 | OWASP Top 10:2025 web application security risks (A01 to A10) |
| OWASP SCVS | OWASP Software Component Verification Standard |
| CWE | MITRE Common Weakness Enumeration, including the CWE Top 25 |
| CISA memory safety | US Cybersecurity and Infrastructure Security Agency guidance on memory-safe languages |
| SLSA | Supply-chain Levels for Software Artifacts 1.2 (build and source tracks) |
| OSPS Baseline | OpenSSF Open Source Project Security Baseline |
| OpenSSF Scorecard | OpenSSF Scorecard checks for open source repositories |
| EU CRA | Regulation (EU) 2024/2847 (Cyber Resilience Act), Article 13, Article 14, Annexes I and II |
| GDPR | Regulation (EU) 2016/679, in particular Article 25 (data protection by design and by default) |
| CycloneDX, SPDX | SBOM formats (CycloneDX includes an ML-BOM for models) |

### AI

| Short name | Source |
|------------|--------|
| OWASP LLM | OWASP Top 10 for Large Language Model Applications 2025 |
| NIST SP 800-218A | SSDF community profile for generative AI and dual-use foundation models |
| NIST AI RMF | NIST AI Risk Management Framework (AI 100-1) |
| ISO/IEC 42001 | AI management systems |
| ISO/IEC 23894 | AI risk management guidance |
| ISO/IEC TR 5469 | Functional safety and AI systems |
| EU AI Act | Regulation (EU) 2024/1689 (Artificial Intelligence Act) |

### Quality

| Short name | Source |
|------------|--------|
| ISO 9001 | ISO 9001:2026, Quality management systems |
| ISO/IEC 90003 | Guidelines for applying ISO 9001 to software |
| ISO/IEC/IEEE 12207 | Software life cycle processes |
| ISO/IEC/IEEE 29148 | Requirements engineering |
| ISO/IEC 25010 | ISO/IEC 25010:2023, product quality model |
| ISO/IEC 25023 | Measurement of system and software product quality |
| ISO/IEC 5055 | Automated source code quality measures |
| ISO/IEC/IEEE 29119 | Software testing (parts 2 and 3: processes and documentation) |
| ISO/IEC 20246 | Work product reviews |
| ISO/IEC/IEEE 26514 | Design and development of information for users |
| ISO/IEC/IEEE 42010 | Architecture description |
| ISO/IEC 33001 | Process assessment |
| EN 301 549, WCAG 2.1, 2.2 | Accessibility requirements for ICT products; Web Content Accessibility Guidelines |

### Safety (Tool Qualification)

| Short name | Source |
|------------|--------|
| IEC 61508-3 | Functional safety, software requirements; 7.4.4 covers support tools; the tool classes T1 to T3 are defined in IEC 61508-4. Sector safety standards use the same concepts; they are not cited, see section 5 |

## 9. Changes

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-11-25 | First draft, one document |
| 0.2 | 2026-11-25 | Split into documents; rules for publishing compliance in public repositories (section 5); only general standards cited, no sector-specific ones; minimum profile for libraries; DEP-12 upstream dependencies; added quality, tool qualification support, Kotlin Multiplatform annex and adoption guide; development by code agents made part of the core and the working model; more sources (IEC 62443-4-1, BSI TR-03185, BSI CON.8, ISO/IEC 27034, ISO/IEC 27701, GDPR, AI management and risk standards) |
| 0.3 | 2026-11-25 | Review fixes: pre-releases (BLD-13); review recorded as a required check (SRC-12); repository backup (SRC-13); developer computers (SRC-14); agent extensions (AGT-19); owner samples agent reviews (AGT-20); person review of security changes (CHG-02); VUL-04 critical limit is now a mitigation or advisory in 7 days and a fix in 30; self-study allowed for training (GOV-06); who approves dependencies (DEP-03); QPL-02 and QCM-01 are SHOULD unless document 07 applies; quarantined tests need a person's approval (QCR-04); TST-04, CHG-01, AGT-02, QDO-04 and QRI-06 retired (merged into others); references updated (ISO 9001:2026, OWASP Top 10:2025, SLSA 1.2, RFC 8174, EU CRA dates and support period); solo-maintainer profile for applications (document 05); ASVS chapters for desktop applications (APP-01); the set for libraries is now reduced to its minimum requirements (library set version 0.4), and an application's own libraries follow that set |
| 0.4 | 2026-11-25 | The solo-maintainer profile is now the one-person profile, open to every application whatever the number of people who take part, so that one person working with code agents is always enough |


