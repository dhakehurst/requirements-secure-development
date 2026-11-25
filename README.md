# Secure Development Requirements

Generic requirements for the development process of software, and for the software it delivers, so
that both meet common security and quality standards (ISO/IEC 27001, NIST SSDF, OWASP, SLSA, the
OpenSSF baseline and the EU Cyber Resilience Act, among others). They are written for the people in
charge of a repository and for the code agents that work in it.

This repository is the single source of the requirements. Other repositories refer to a fixed
version of them; they do not copy them.

## The Two Sets

| Set | For | Start with |
|-----|-----|------------|
| [Libraries](libraries/README.md) | repositories that publish a library, package, plug-in or other component that other software builds on | [libraries/README.md](libraries/README.md) |
| [Applications](applications/README.md) | repositories that deliver software that people run: desktop or mobile applications, command-line tools, servers and web services | [applications/README.md](applications/README.md) |

Both sets use the same requirement ids where a requirement is the same. Each set is complete on its
own; a repository follows one set.

## Using This Set

1. Choose the set that fits the repository.
2. Add a reference to the repository's README (or `SECURITY.md`). It names the set, its version
   tag and the commit hash of that tag, so that the text cannot change under the reference:

   ```markdown
   ## Secure Development Requirements

   This repository follows the Secure Development Requirements for <Libraries | Applications>,
   version <x.y>: <URL of this repository>/tree/<set>-v<x.y> (commit <full commit hash>).
   Compliance checklist: [docs/security/compliance-checklist.md](docs/security/compliance-checklist.md)
   ```

3. Point the repository's agent instruction file (for example `CLAUDE.md` or `AGENTS.md`) to the
   same version, and allow agents network access to this repository. Agents read the documents
   there; they MAY fetch them into a scratch area but never commit a copy.
4. Fill in the checklist of the set in the repository itself. The checklist is the repository's own
   record, not a copy of the requirements. Follow the set's adoption guide for an existing
   repository, and its rules for what a public checklist may show.

To move to a new version: change the reference, check the checklist against the changes listed in
the new version, and merge the update as a reviewed change.

## Versions

- Each set has its own version, released as a tag `libraries-v<x.y>` or `applications-v<x.y>`.
- Tags are never moved or deleted, and history is never rewritten, so that every version a
  repository has referred to can always be read.
- Versions below 1.0 are drafts.
- Each set's README lists the changes of every version; [CHANGELOG.md](CHANGELOG.md) lists the
  releases.

## Licence

The text is licensed under [CC BY 4.0](LICENSE): it may be used and adapted, with credit.
