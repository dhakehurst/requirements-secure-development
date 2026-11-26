# Maintaining the Requirement Sets

This file is for anyone, a person or a code agent, who reviews the sets for accuracy or changes
them. It records where the requirements come from, why the main decisions were made, the rules for
editing, and the sources to watch. Read it before proposing a change.

## 1. Repository Layout

| Path | Content |
|------|---------|
| `README.md` | How other repositories use the sets; versions |
| `libraries/` | The set for libraries: README, 01 requirements, 02 guidance for code agents, A1 Kotlin and Gradle annex, adoption guide |
| `applications/` | The set for applications: README, 01 core, 02 code agents, 03 quality, 05 applications and services (with the one-person profile), 06 LLM software, 07 tool qualification support, A1 Kotlin and Gradle annex, adoption guide |
| `tools/check.py` | Consistency check, run by CI on every push and merge request |
| `MAINTAINING.md` | This file |
| `AGENTS.md` | Instructions for code agents that work in this repository |
| `CLAUDE.md` | Points Claude Code to `AGENTS.md` |

## 2. Reviewing for Accuracy

A review checks that each requirement says what its sources say, that the sources are current, and
that the decisions in section 4 still hold.

1. For each requirement, read its *Sources* field and compare the requirement with the cited clause
   or practice. A requirement MAY be stricter or more specific than its source, but MUST NOT
   contradict it or claim a source says something it does not.
2. Check each source in section 3 for a newer edition. Where there is one, note what changed and
   which requirements cite it.
3. For the library set, check the OSPS Baseline mapping (libraries README, section 8) against the
   current Baseline version.
4. Check that nothing in the repository names a user, customer, programme or sector of the sets,
   and that no sector-specific standard is cited (section 4, D5).
5. Record the findings as issues or as one merge request per finding, each with the source and
   clause that shows the problem.

Many ISO, IEC and BSI standards are not free. A reviewer without access to a standard says so
in the finding, and checks it against the publisher's abstract and table of contents only.

## 3. Sources

"Cited" is the edition the sets name. "Current" is what the publisher's page showed on the date in
"Checked". "Sets": L = libraries, A = applications. The ISO pages are the catalogue entries; the
texts are sold by ISO and national bodies.

### Wording

| Short name | Cited | Current | Checked | Sets | Link |
|------------|-------|---------|---------|------|------|
| RFC 2119, RFC 8174 | BCP 14 | BCP 14 | 2026-11-25 | L, A | https://www.rfc-editor.org/info/bcp0014 |

### Security

| Short name | Cited | Current | Checked | Sets | Link |
|------------|-------|---------|---------|------|------|
| ISO 27001 | 2022 | 2022 | 2026-11-25 | L, A | https://www.iso.org/standard/iso-iec-27000-family |
| ISO 27002 | 2022 | 2022 | 2026-11-25 | A | https://www.iso.org/standard/75652.html |
| ISO/IEC 27034 | no edition (part 1) | 27034-1:2011 | 2026-11-25 | A | https://www.iso.org/standard/44378.html |
| ISO/IEC 27701 | 2025 | 2025 | 2026-11-25 | A | https://www.iso.org/standard/27701 |
| ISO/IEC 29147 | no edition | 2018 (revision started) | 2026-11-25 | L, A | https://www.iso.org/standard/72311.html |
| ISO/IEC 30111 | no edition | 2019 | 2026-11-25 | L, A | https://www.iso.org/standard/69725.html |
| ISO/IEC 5230 | no edition | 2020 | 2026-11-25 | L, A | https://www.iso.org/standard/81039.html |
| ISO/IEC 18974 | no edition | 2023 | 2026-11-25 | L, A | https://www.iso.org/standard/86450.html |
| IEC 62443-4-1 | no edition | 2018 | 2026-11-25 | L, A | https://webstore.iec.ch/en/publication/33615 |
| SSDF | 1.1 (SP 800-218) | 1.1; 1.2 is a draft (SP 800-218 Rev. 1, December 2025) | 2026-11-25 | L, A | https://csrc.nist.gov/pubs/sp/800/218/r1/ipd |
| BSI TR-03185 | no version | part 1 (2024) | 2026-11-25 | A | https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03185/TR-03185_node.html |
| BSI TR-03183-2 | 2.1.0 | 2.1.0 (3 September 2025) | 2026-11-25 | L, A | https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03183/TR-03183_node.html |
| BSI CON.8 | no edition | Edition 2023 | 2026-11-25 | A | https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/03_CON_Konzepte_und_Vorgehensweisen/CON_8_Software_Entwicklung_Edition_2023.pdf |
| SAMM | 2 | 2 | 2026-11-25 | A | https://owaspsamm.org/model/ |
| ASVS 5.0 | 5.0 | 5.0.0 | 2026-11-25 | L, A | https://asvs.owasp.org/ |
| OWASP Top 10 | 2025 | 2025 | 2026-11-25 | A | https://top10.owasp.org/2025/ |
| OWASP SCVS | no version | not checked | 2026-11-25 | L, A | https://scvs.owasp.org/ |
| CWE Top 25 | no year | 2025 | 2026-11-25 | L, A | https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25.html |
| CISA memory safety | no date | not checked | 2026-11-25 | A | https://www.cisa.gov/resources-tools/resources/case-memory-safe-roadmaps |
| SLSA | 1.2 | 1.2 | 2026-11-25 | L, A | https://slsa.dev/spec/v1.2/ |
| OSPS Baseline | 2026.08.28 (L); no version (A) | 2026.08.28 | 2026-11-25 | L, A | https://baseline.openssf.org/versions/2026-08-28 |
| OpenSSF Scorecard | no version | not checked | 2026-11-25 | A | https://scorecard.dev/ |
| EU CRA | Regulation (EU) 2024/2847 | in force; reporting from 11 September 2026 | 2026-11-25 | L, A | https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng |
| GDPR | Regulation (EU) 2016/679 | in force | 2026-11-25 | L, A | https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32016R0679 |
| CycloneDX | no version | 1.7 | 2026-11-25 | L, A | https://cyclonedx.org/specification/overview/ |
| SPDX | no version | 3.0.1 (3.1 in review) | 2026-11-25 | L, A | https://spdx.dev/use/specifications/ |

### AI

| Short name | Cited | Current | Checked | Sets | Link |
|------------|-------|---------|---------|------|------|
| OWASP LLM | 2026 | 2026 (published September 2026; final or draft not stated) | 2026-11-25 | L, A | https://genai.owasp.org/top-10-for-llm-applications-2026/ |
| OWASP Agentic | 2026 | 2026 (final or draft not stated) | 2026-11-25 | A | https://genai.owasp.org/top-10-for-agentic-applications-2026/ |
| NIST SP 800-218A | no edition | final (2024) | 2026-11-25 | A | https://csrc.nist.gov/news/2024/nist-publishes-sp-800-218a |
| NIST AI RMF | AI 100-1 | 1.0 | 2026-11-25 | A | https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10 |
| ISO/IEC 42001 | no edition | 2023 | 2026-11-25 | A | https://www.iso.org/standard/42001 |
| ISO/IEC 23894 | no edition | 2023 | 2026-11-25 | A | https://www.iso.org/standard/77304.html |
| ISO/IEC TR 5469 | no edition | 2024 | 2026-11-25 | A | https://www.iso.org/standard/81283.html |
| EU AI Act | Regulation (EU) 2024/1689 | in force, consolidated 2026-07-27 | 2026-11-25 | A | https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng |

### Quality

| Short name | Cited | Current | Checked | Sets | Link |
|------------|-------|---------|---------|------|------|
| ISO 9001 | 2026 | 2026 | 2026-11-25 | A | https://www.iso.org/standard/9001 |
| ISO/IEC 90003 | no edition | ISO/IEC/IEEE 90003:2018 (for ISO 9001:2015) | 2026-11-25 | A | https://www.iso.org/standard/74348.html |
| ISO/IEC/IEEE 12207 | 2026 | 2026 (edition 2, April 2026) | 2026-11-25 | A | https://www.iso.org/standard/90219.html |
| ISO/IEC/IEEE 29148 | no edition | 2018 (revision at DIS) | 2026-11-25 | A | https://www.iso.org/standard/72089.html |
| ISO/IEC 25010 | 2023 | 2023 | 2026-11-25 | A | https://www.iso.org/standard/78176.html |
| ISO/IEC 25023 | no edition | 2016 (to be replaced by ISO/IEC 25000-23, at DIS) | 2026-11-25 | A | https://www.iso.org/standard/35747.html |
| ISO/IEC 5055 | no edition | 2021 | 2026-11-25 | A | https://www.iso.org/standard/80623.html |
| ISO/IEC/IEEE 29119 | parts 2 and 3, no edition | 2021 | 2026-11-25 | A | https://www.iso.org/standard/79428.html |
| ISO/IEC 20246 | no edition | 2017 | 2026-11-25 | L, A | https://www.iso.org/standard/67407.html |
| ISO/IEC/IEEE 26514 | no edition | 2022 | 2026-11-25 | A | https://www.iso.org/standard/77451.html |
| ISO/IEC/IEEE 42010 | no edition | 2022 | 2026-11-25 | A | https://www.iso.org/standard/74393.html |
| ISO/IEC 33001 | no edition | 2015 | 2026-11-25 | A | https://www.iso.org/standard/54175.html |
| EN 301 549 | no version | V3.2.1 harmonised; V4.1.0 in draft | 2026-11-25 | A | https://www.etsi.org/human-factors-accessibility/en-301-549-v3-the-harmonized-european-standard-for-ict-accessibility |
| WCAG | 2.1, 2.2 | 2.2 (W3C Recommendation) | 2026-11-25 | A | https://www.w3.org/TR/WCAG22/ |

### Safety

| Short name | Cited | Current | Checked | Sets | Link |
|------------|-------|---------|---------|------|------|
| IEC 61508-3 | no edition, 7.4.4 | 2010 | 2026-11-25 | A | https://webstore.iec.ch/publication/5517 |

## 4. Decisions

These are the main decisions behind the sets, with their reasons. A change that reverses one of
them states the reason in its merge request, and updates this section.

- **D1 Two sets with the same ids.** Libraries and applications need different amounts of process,
  but a requirement means the same in both. An id is never reused for a different requirement.
- **D2 The library set is the minimum.** It holds only requirements that protect the library's
  users, each MUST, each saying who does it, with as little ongoing work as possible for the
  person. Everything else is guidance for code agents (document 02), which costs the person
  nothing. Only commercial support moves a library to the fuller requirements of the application
  set.
- **D3 One person and code agents is always enough.** The sets never require a second person or a
  minimum number of maintainers, because the work is often done by one volunteer. The number of
  volunteers makes no difference; commercial support does.
- **D4 No response or fix times for voluntary work.** Libraries (LIB-11) and voluntarily maintained
  applications (VUL-10) handle reports on a best-effort basis. Fixed times, including a fallback
  disclosure deadline, were rejected because they are a time limit that a volunteer cannot promise.
  Users that need guaranteed times handle the risk in their own product.
- **D5 Only general standards.** The sets cite general or multi-sector standards only. Sector
  standards are not cited, because citing them would reveal where the sets, or the software built
  with them, are used. The library set has no tool qualification document for the same reason; its
  README says libraries are not developed to a functional safety standard.
- **D6 Public compliance, private gaps.** A public repository shows its checklist with status,
  public evidence and target dates only. Reasons for gaps, accepted risks and unfixed
  vulnerabilities are kept in a private record (GOV-09, GOV-10).
- **D7 Review by another agent session, recorded as a check.** Every change is reviewed by a
  separate session or a person (SRC-05). Where one account pushes all changes, the review is
  recorded as a required status check, because hosting platforms do not let an account approve its
  own merge request. In the application set the person also reviews security-relevant changes
  (CHG-02) and samples agent reviews (AGT-20).
- **D8 OSPS Baseline Level 1 for libraries, not Level 2.** The library set meets Level 1 (libraries
  README, section 8), so a library can claim it. Level 2 expects at least two maintainers and a
  response timeframe, which conflicts with D3 and D4.
- **D9 Build tool wrappers.** OSPS-QA-05.02 forbids unreviewable binaries and does not mention
  build tool wrappers. LIB-16 allows a wrapper jar only where CI checks it against its publisher's
  checksum. This is the sets' own reading, not the Baseline's.
- **D10 New runtime dependencies are approved by the person; access is not reviewed yearly.** The
  approval (DEP-03) is the main guard against a harmful dependency and is kept. A yearly access
  review was dropped from the library set (SRC-02), since access is set when someone joins or
  leaves.
- **D11 Referenced, not copied.** Other repositories refer to a fixed version of a set and never
  copy it (GOV-03), so that there is one source. Drafts (below 1.0) are referenced by full commit
  hash only; tags start at 1.0. There is no change log: the changes are in the commit history and,
  from 1.0, in the release notes of each tag.
- **D12 SSDF 1.1, not the 1.2 draft.** Drafts are not cited as sources; they are on the watch list
  (section 6).
- **D13 OWASP LLM ids mapped by subject.** When the 2026 list renumbered the risks, each citation
  was moved to the 2026 item with the same subject, since OWASP gives no mapping: 2025 LLM03
  supply chain is now LLM04, LLM04 poisoning LLM05, LLM05 output handling LLM10, LLM06 excessive
  agency LLM03, LLM07 system prompt leakage LLM08 (hidden context exposure), LLM08 vector and
  embedding LLM09, LLM09 misinformation LLM07, LLM10 unbounded consumption LLM06.
- **D14 Releases are published from CI only.** Publishing from a person's own computer was
  considered and rejected: a release built and signed in CI can be traced to its source, and after
  a one-off setup each release is one approval. The signing key is a release-only key held in the
  CI system's protected secrets, not a personal key (BLD-06, LIB-01, KMP-21).

## 5. Editing Rules

- **Ids.** An id is never reused or renumbered. A requirement that is removed stays as a line
  "**XXX-nn (retired in x.y).** Merged into ..." in its document.
- **Both sets.** Where a requirement exists in both sets, a change to it is made in both, or the
  merge request says why the sets differ.
- **Format of a requirement.** `- **ID (LEVEL) Title.** Text. *Who:* ... *Evidence:* ...
  *Sources:* ...` (the library set also has *Who:* on every requirement and *OSPS Level 1:* where
  it applies). Levels are MUST,
  MUST NOT, SHOULD, SHOULD NOT and MAY, as in RFC 2119 and RFC 8174.
- **Checklists.** Each document with requirements ends with a checklist that lists every
  requirement of that document, with the same level and title. `tools/check.py` checks this.
- **Versions.** A change to the meaning of any requirement raises the set's version. The version
  and date are given in the set's README and at the top of every document of the set, and are
  changed together.
- **Language.** British English. Plain, short sentences. Requirement names and file names in code
  formatting.
- **Lines.** Lines wrap at 100 characters, except table rows and code blocks.
- **Public text.** Nothing names a person, company, customer, programme, product or sector that
  uses the sets (D5, D6). Examples use generic names.
- **Copyrighted sources.** Requirements are written in our own words. Text from a source is not
  copied, in particular from sources under share-alike or other restrictive licences.
- **One change, one merge request.** Each merge request covers one topic, says which sources it
  relies on, and passes `tools/check.py`.

## 6. Watch List

Sources that are expected to change, and what to do when they do.

| Source | Expected change | Then |
|--------|-----------------|------|
| SSDF 1.2 (SP 800-218 Rev. 1) | final version | update the SSDF row of both READMEs and check the practice ids cited |
| OWASP LLM and Agentic Top 10 | next version | move each citation by subject (D13) |
| OSPS Baseline | new version | check the Level 1 mapping (libraries README, section 8) and the *OSPS Level 1* fields |
| ISO/IEC/IEEE 12207 | 2026 edition is cited, but its table of contents was not checked | check that the process names cited in document 03 (applications) still exist |
| ISO/IEC 25023 | to be replaced by ISO/IEC 25000-23 | change the citation when it is published |
| ISO/IEC/IEEE 29148, ISO/IEC 29147 | revisions in progress | check the citations when published |
| BSI TR-03183-2 | 2.1.0 is cited, but its field list was not read (the PDF could not be fetched) | check the SBOM fields and formats required (DEP-09) against 2.1.0 |
| EN 301 549 | V4 | check the WCAG level it refers to (QRI-05) |
| EU CRA | implementing acts and harmonised standards | check the reporting and support period requirements |
| OWASP Agent Control Standard | published by the GenAI Security Project in 2026, status not checked | consider it as a source for the agent requirements (AGT) |

## 7. Checks

`tools/check.py` runs in CI (`.github/workflows/check.yml`) and can be run locally with
`python3 tools/check.py`. It checks that ids are defined once, that checklists and the one-person
profile match the requirements, that every id mentioned exists, that versions agree, and the line
length. It does not check meaning or sources; that is the review of section 2.
