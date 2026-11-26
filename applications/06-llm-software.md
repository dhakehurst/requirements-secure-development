# 06 Software That Uses LLMs

Part of the Secure Development Requirements for Applications, version 0.7 (draft), 2026-11-26. Read
the [README](README.md) first: it gives the wording rules, the working model, the terms and the
sources.

## Scope

Applies in addition to documents 01 to 03 and 05 when the delivered software sends data to a large
language model (LLM), uses retrieval (RAG), or lets a model call tools.

## Requirements

- **AI-01 (MUST) Threat model covers OWASP LLM Top 10.** The threat model (DES-02) covers each item
  of the OWASP Top 10 for LLM Applications 2026 (LLM01 to LLM10) and records which measures apply.
  *Sources:* OWASP Top 10 for LLM 2026; ISO 27001 A.8.27; ISO/IEC 42001; ISO/IEC 23894; NIST AI RMF.
- **AI-02 (MUST) External content untrusted (prompt injection).** Content that reaches the model
  from outside the user's own instruction (documents, retrieved data, web pages, tool results, file
  names) is treated as untrusted. It is kept separate from instructions in the prompt, and the
  design assumes that it may contain instructions meant to take over the model (prompt injection).
  *Sources:* OWASP LLM01; NIST SP 800-218A.
- **AI-03 (MUST) Model output validated.** Model output is treated as untrusted input (COD-02): it
  is validated before it is used in queries, commands, file paths, code, markup or calls to other
  systems, and encoded before it is shown. *Sources:* OWASP LLM10; COD-03, COD-04.
- **AI-04 (MUST) Least-privilege tools.** Tools that the model can call are limited to what the use
  case needs, each with the least privileges (for example read-only access where reading is enough),
  and with the rights of the current user, never more. *Sources:* OWASP LLM03 (Excessive Agency);
  ISO 27001 A.8.2.
- **AI-05 (MUST) User confirms lasting actions.** Actions with effects that are hard to undo
  (changing or deleting data, sending messages, spending money, running programs) need explicit
  confirmation by the user, shown with what will happen. *Sources:* OWASP LLM03; EU AI Act human
  oversight principles.
- **AI-06 (MUST) Data sent only to approved models.** Data is sent to a model only where the model's
  location and operator are approved for that data's classification. Sensitive data is not sent to
  external model services unless that is approved. The documentation states where model calls go
  (PRD-02). *Sources:* OWASP LLM02; ISO 27001 A.5.14, A.5.23, A.8.12.
- **AI-07 (MUST NOT) No secrets in prompts.** Secrets and access rights MUST NOT be placed in
  prompts, system prompts or tool descriptions, and the system prompt is not relied on to keep
  anything secret or to enforce access control. *Sources:* OWASP LLM08.
- **AI-08 (MUST) Retrieval keeps access rights.** Retrieval (RAG) and vector stores enforce the same
  access rights as the source data: a user's query retrieves only what that user may see. Stored
  embeddings are protected as the source text they came from. *Sources:* OWASP LLM09, LLM02; APP-03.
- **AI-09 (MUST) Models from approved sources, in SBOM.** Models are obtained only from approved
  sources, with a recorded version and checksum, and are listed in the SBOM (DEP-09) like other
  dependencies. Their licences are checked (DEP-08). *Sources:* OWASP LLM04, LLM05; SSDF PW.4;
  CycloneDX ML-BOM.
- **AI-10 (MUST) Bounded model use.** Use of the model is bounded: limits on input size, output
  size, number of tool calls per request, time and cost. *Sources:* OWASP LLM06; COD-10.
- **AI-11 (MUST) Sources shown, model answers marked.** Answers that users act on show their sources
  (which data the answer is based on), and the user interface makes clear that answers come from a
  model and may be wrong. *Sources:* OWASP LLM07; EU AI Act transparency obligations.
- **AI-12 (SHOULD) Evaluation cases.** The behaviour of the model in the application is tested with
  a fixed set of evaluation cases, including prompt injection attempts and requests for data the
  user may not see, and the evaluation is re-run when the model, the prompts or the tools change.
  *Sources:* NIST SP 800-218A; OWASP LLM01, LLM07.
- **AI-13 (MUST) Prompt logging controlled.** Prompts and model responses are logged only as allowed
  by DES-05 and COD-07, with the same protection as the data they contain. *Sources:* ISO 27001
  A.8.15, A.8.12.

## Checklist

Status: **met**, **partly**, **not met**, **n/a**. Every "not met" MUST and every "n/a" needs a
short reason; a "not met" MUST also needs an exception (GOV-05). In a public repository, the
evidence column follows GOV-09: status, public links and target dates only.

| Id | Level | Requirement | Status | Evidence or reason |
|----|-------|-------------|--------|--------------------|
| AI-01 | MUST | Threat model covers OWASP LLM Top 10 | | |
| AI-02 | MUST | External content untrusted (prompt injection) | | |
| AI-03 | MUST | Model output validated | | |
| AI-04 | MUST | Least-privilege tools | | |
| AI-05 | MUST | User confirms lasting actions | | |
| AI-06 | MUST | Data sent only to approved models | | |
| AI-07 | MUST NOT | No secrets in prompts | | |
| AI-08 | MUST | Retrieval keeps access rights | | |
| AI-09 | MUST | Models from approved sources, in SBOM | | |
| AI-10 | MUST | Bounded model use | | |
| AI-11 | MUST | Sources shown, model answers marked | | |
| AI-12 | SHOULD | Evaluation cases | | |
| AI-13 | MUST | Prompt logging controlled | | |

