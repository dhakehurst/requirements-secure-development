# 07 Tool Qualification Support

Part of the Secure Development Requirements for Applications, version 0.4 (draft), 2026-11-25. Read
the [README](README.md) first: it gives the wording rules, the working model, the terms and the
sources.

## Scope

Applies when the software is not itself safety-related, but may be used to develop, verify or
document systems that are safety-related. This covers engineering tools, and libraries that such
tools are built from, where the developer does not know every use.

Safety standards do not make the tool developer responsible for qualifying the tool. They make the
**user** of the tool responsible for deciding how much confidence the tool needs for their use, and
for qualifying it. What the user needs from the developer is evidence: what the tool does, how it
was verified, which version they have, and which faults are known. These requirements make sure that
the evidence exists, so that a user can qualify the software without having to repeat the
developer's work.

The common ideas in the safety standards are:

- **Tool impact**: can a fault in the tool put an error into the product (for example a generator or
  a transformation), or only fail to find one (for example a checker or an analysis)?
- **Error detection**: how likely it is that such an error is found by other means.
- From these the user derives a tool class: IEC 61508 uses classes T1 to T3 (defined in IEC 61508-4
  and used in IEC 61508-3 7.4.4). The sector standards derived from IEC 61508, and other safety
  standards, use the same ideas with their own classes or levels; the user applies the one for their
  sector.

## Requirements (TQS)

- **TQS-01 (MUST) Intended use and status stated.** The documentation states what the software is
  for, that it was not developed to a functional safety standard, and that a user who uses it in the
  development of a safety-related system is responsible for deciding whether it needs to be
  qualified for that use. *Sources:* IEC 61508-3 7.4.4.
- **TQS-02 (MUST) Functions specified.** The functions of the software are specified as requirements
  (core and quality documents, QPL-02), so that a user can say which functions they rely on.
  *Sources:* IEC 61508-3 7.4.4 (specification or manual).
- **TQS-03 (MUST) Possible failures described.** For each main function, the documentation says what
  kinds of wrong result a fault could cause (wrong output, missing output, missed finding), and what
  the user can do to detect them. This is the information a user needs to judge tool impact and
  error detection. *Sources:* IEC 61508-3 7.4.4.
- **TQS-04 (MUST) Verification evidence per release.** For each release, the test results are kept
  and can be given to users, traced to the requirements they verify (QCM-01). *Sources:* IEC 61508-3
  7.4.4 (evidence of conformance to specification).
- **TQS-05 (MUST) Exact version identifiable.** The user can find the exact version they use, and
  the developer can rebuild that version from its archived source and build (core BLD-05, BLD-11).
  The software reports its version, and tools record it in their outputs or logs where outputs are
  kept. *Sources:* IEC 61508-3 7.4.4 (configuration management of tools).
- **TQS-06 (MUST) Known problems published.** The known problems list (QCM-03) states for each
  problem whether it can cause a wrong result, which versions are affected, and how to avoid it.
  *Sources:* IEC 61508-3 7.4.4 (increased confidence from use, which needs records of faults).
- **TQS-07 (MUST) Users told of faults that give wrong results.** When a fault is found that can
  give a wrong result without warning, users are told in the same way as for vulnerabilities (core
  VUL-05), with the affected versions. *Sources:* IEC 61508-3 7.4.4.
- **TQS-08 (MUST) Behaviour changes listed.** The change log (BLD-10) lists every change to the
  results the software produces for the same input, so that a user can judge whether a new version
  needs to be re-qualified. *Sources:* IEC 61508-3 7.4.4.
- **TQS-09 (MUST) Deterministic results.** For the same input, configuration and version, the
  software gives the same result. Where it cannot (for example results from a language model or
  anything that depends on time), the documentation says so, and the output is marked. *Sources:*
  IEC 61508-3 7.4.4.
- **TQS-10 (MUST) Invalid input reported.** Invalid or unsupported input gives a clear error. It
  never gives a result that looks valid but is silently wrong or incomplete. *Sources:* IEC 61508-3
  7.4.4.
- **TQS-11 (SHOULD) Results can be checked.** The software makes its results checkable by other
  means, for example with reports, traces from input to output, or a separate check function.
  *Sources:* IEC 61508-3 7.4.4.
- **TQS-12 (SHOULD) Qualification test suite.** The tests that verify the main functions can be run
  by a user in their own environment, with documented expected results, so that they can be used as
  part of a qualification kit. *Sources:* IEC 61508-3 7.4.4.
- **TQS-13 (SHOULD) Long-term availability.** Released versions stay available for at least the
  support period (core VUL-07), and their source, build environment and dependencies are archived so
  that the version can be rebuilt. *Sources:* IEC 61508-3 7.4.4.
- **TQS-14 (MUST) Use of AI in results disclosed.** Where a function uses a language model or other
  machine learning, the documentation says which functions, and their results are marked as such,
  because their failure behaviour is different from that of conventional code. *Sources:* ISO/IEC TR
  5469 (functional safety and AI systems); TQS-09.

## Checklist

Status: **met**, **partly**, **not met**, **n/a**. Every "not met" MUST and every "n/a" needs a
short reason; a "not met" MUST also needs an exception (GOV-05). In a public repository, the
evidence column follows GOV-09: status, public links and target dates only.

| Id | Level | Requirement | Status | Evidence or reason |
|----|-------|-------------|--------|--------------------|
| TQS-01 | MUST | Intended use and status stated | | |
| TQS-02 | MUST | Functions specified | | |
| TQS-03 | MUST | Possible failures described | | |
| TQS-04 | MUST | Verification evidence per release | | |
| TQS-05 | MUST | Exact version identifiable | | |
| TQS-06 | MUST | Known problems published | | |
| TQS-07 | MUST | Users told of faults that give wrong results | | |
| TQS-08 | MUST | Behaviour changes listed | | |
| TQS-09 | MUST | Deterministic results | | |
| TQS-10 | MUST | Invalid input reported | | |
| TQS-11 | SHOULD | Results can be checked | | |
| TQS-12 | SHOULD | Qualification test suite | | |
| TQS-13 | SHOULD | Long-term availability | | |
| TQS-14 | MUST | Use of AI in results disclosed | | |
