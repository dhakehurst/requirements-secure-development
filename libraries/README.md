# Secure Development Requirements for Libraries

Version 0.5 (draft), 2026-11-25

## 1. Purpose

This set of documents gives the requirements that a library repository MUST meet so that its
process, and the library it publishes, meet common security standards, with the least extra effort
for the person who maintains it. It is generic: it applies to any library repository, whatever the
product or the organisation.

It is for repositories that publish a library, package, plug-in or other component that other
software builds on, and that are maintained voluntarily, however many people take part, with most of
the work done by code agents. Applications use the separate set for applications.

The set has two kinds of content:

- **Requirements** (document 01): few, all MUST, each with a clear owner (person, agent or CI). Most
  of the person's part is done once per repository.
- **Guidance for code agents** (document 02 and the second part of annex A1): detailed, not a
  checklist, and costs the person nothing. It tells the agents how to do a good job.

Libraries developed under this set are not developed to a functional safety standard. A user who
uses one in developing a safety-related system decides whether it needs to be qualified for that
use.

## 2. The Documents

| Document | Applies | Ids |
|----------|---------|-----|
| [01 Requirements](01-requirements.md) | always | GOV, SRC, DEP, BLD, TST, VUL, LIB, AGT |
| [02 Guidance for code agents](02-agent-guidance.md) | always (guidance, not requirements) | (none) |
| [A1 Kotlin Multiplatform annex](A1-kotlin-multiplatform-annex.md) | the repository uses Kotlin Multiplatform and Gradle | KMP |
| [Adoption guide](adoption-guide.md) | how to bring a repository into line, and the person's steps | (none) |

The ids are the same as in the set for applications, so that a requirement means the same in both.
Where support for a library is ever offered commercially, it applies instead the core, agent and
quality documents (01 to 03) of the set for applications, with these documents.

Third-party dependencies, including the language runtime and its standard library, are not required
to meet these requirements: they are checked when added (DEP-03) and scanned (DEP-05).

## 3. Requirement Wording

The key words MUST, MUST NOT, SHOULD and MAY are used as in RFC 2119 and RFC 8174 (they have this
meaning only when written in capitals). All requirements in document 01 are MUST or MUST NOT.

A requirement that is not met is marked "not met" in the checklist, with a target date. The reason,
the risk and the plan are written in a private record (for example a private repository, or the
hosting platform's private security advisories), which the owner accepts and can show on request. In
a private repository the record MAY be the checklist itself.

Each requirement has an id, a level, a short title, the requirement, who does it, often the
**evidence** that shows it is met, and the **sources** it comes from (section 7). Ids are stable
across versions: a requirement that is removed keeps its id unused.

## 4. Working Model

1. **The person asks for the work** and stays responsible for it. The owner of the repository is
   always a person.
2. **A code agent session writes the change** in its own sandbox, with credentials limited to the
   task, following documents 01 and 02.
3. **A separate code agent session reviews the change** (SRC-05). It is given the change, its reason
   and these documents, not the reasoning of the session that wrote it. A session never reviews its
   own change.
4. **The person approves** only what document 01 names: new runtime dependencies, changes to CI,
   publishing or agent configuration, and quarantined tests. The person also starts releases,
   publishes advisories, and does the one-off settings. Document 01, "The Person's Part", lists all
   of it.

## 5. Public Repositories

The requirements and each repository's filled-in checklist are meant to be published in the
repository, so that anyone can see that it complies. Publishing them must not weaken the security it
shows (GOV-09, GOV-10, VUL-09, AGT-18):

- **Public**: the requirements, the status of each, links to public evidence (CI results, published
  SBOMs, signatures, `SECURITY.md`), target dates for open items.
- **Private**: reasons and plans for open items, vulnerabilities before their fix is released, names
  and contacts of people beyond public handles, internal systems, and who uses the software.
- **Not named in public**: customers, programmes, sectors or organisations that use the software.
  That is why these documents cite only general standards, never sector-specific ones.

## 6. Terms

- **Repository**: the version-controlled source of one library, with its build and release
  configuration.
- **Owner** or **person**: the person accountable for the repository (GOV-01).
- **Code agent**: an AI assistant that reads, writes, builds, tests or commits code. An **agent
  session** is one run of a code agent with its own context and workspace.
- **Agent extension**: an MCP server, plug-in, skill, hook or other component that adds tools,
  instructions or automatic actions to a code agent.
- **Release**: a version published to the registry, or given to anyone outside the development team.
- **Dependency**: any third-party component used to build, test or run the library, including build
  plug-ins, CI actions and AI models.
- **Secret**: a password, token, private key, API key or other credential.

## 7. Sources

The requirements and the guidance are derived from these public standards and guides. Where a source
is a management system standard (ISO 27001), the requirements here are one way of meeting its
controls for software development; they do not replace an organisation's own policies.

| Short name | Source |
|------------|--------|
| ISO 27001 | ISO/IEC 27001:2022, Information security management systems, Annex A |
| ISO/IEC 29147, 30111 | Vulnerability disclosure; vulnerability handling processes |
| ISO/IEC 5230, 18974 | OpenChain licence compliance; OpenChain security assurance |
| ISO/IEC 20246 | Work product reviews |
| IEC 62443-4-1 | Secure product development life cycle requirements |
| SSDF | NIST SP 800-218, Secure Software Development Framework 1.1 (practices PO, PS, PW, RV). Version 1.2 (SP 800-218 Rev. 1) was still a draft when this version was written; its practice ids may differ |
| SLSA | Supply-chain Levels for Software Artifacts 1.2 (build and source tracks) |
| OSPS Baseline | OpenSSF Open Source Project Security Baseline |
| OWASP SCVS | OWASP Software Component Verification Standard |
| ASVS 5.0 | OWASP Application Security Verification Standard 5.0 |
| CWE | MITRE Common Weakness Enumeration, including the CWE Top 25 (document 02) |
| OWASP LLM | OWASP Top 10 for Large Language Model Applications 2025 (document 02) |
| EU CRA | Regulation (EU) 2024/2847 (Cyber Resilience Act), Article 14, Annexes I and II |
| GDPR | Regulation (EU) 2016/679, Article 25 (data protection by design and by default) |
| BSI TR-03183-2 | German Federal Office for Information Security, Technical Guideline on SBOMs |
| CycloneDX, SPDX | SBOM formats |

## 8. Changes

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-11-25 | First draft, one document |
| 0.2 | 2026-11-25 | Split into documents; public repository rules; minimum profile for libraries |
| 0.3 | 2026-11-25 | Review fixes (see the set for applications); minimum profile 31 requirements; no response or fix time limits for voluntarily maintained libraries (LIB-11) |
| 0.4 | 2026-11-25 | The set is reduced to the minimum profile: document 01 holds all 31 requirements, all MUST, each saying who does it, with a list of the person's part. The rest of the former documents 01 to 04 and 06 became guidance for code agents (document 02), with no checklist. Deterministic results, clear errors, version reporting and marking results that come from a language model are in the guidance. Annex A1 split into practices for the requirements and guidance; no separate checklist |
| 0.5 | 2026-11-25 | The set applies to every voluntarily maintained library, whatever the number of maintainers; only commercial support moves a library to the fuller requirements |
