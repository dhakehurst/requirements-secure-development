# A1 Kotlin and Gradle Annex

Part of the Secure Development Requirements for Applications, version 0.7 (draft), 2026-11-26. Read
the [README](README.md) first: it gives the wording rules, the working model, the terms and the
sources.

## Scope

Applies to repositories written in Kotlin and built with Gradle: Kotlin Multiplatform (JVM,
JavaScript, WebAssembly, Native) or Kotlin for the JVM only. In a JVM-only repository, entries
marked *Multiplatform only* do not apply, and the parts of other entries about JS, wasm or native
targets do not apply. It adds no new requirements, but some entries are stricter than the
requirement they implement, and say so. It says how the requirements of the other documents are met
in such a repository, so that every repository does it the same way. Each entry names the
requirement it implements. Where an entry here is not followed, the requirement still applies and
has to be met another way. Under a profile that turns a MUST into a SHOULD (the one-person profile),
an entry here has the level of the requirement it implements. KMP-21 is used only in the set for
libraries.

Tool and plug-in names are given as examples of what is in common use. Use the current maintained
version, and check that a named option still exists in that version before relying on it.

## Practices (KMP)

### Dependencies

- **KMP-01 (MUST) Versions in one catalogue.** All dependency and plug-in versions are in the Gradle
  version catalogue (`gradle/libs.versions.toml`), as exact versions. No dynamic versions (`+`,
  `latest.release`, ranges) and no snapshot versions in release builds. *Implements:* DEP-02,
  DEP-07.
- **KMP-02 (MUST) Gradle dependency verification.** `gradle/verification-metadata.xml` is committed,
  with SHA-256 checksums (and PGP keys where the publisher signs) for every artefact, including
  plug-ins and their dependencies. The build fails on a missing or wrong checksum. Updating the file
  is part of the same reviewed change that updates the dependency, and is never done to make an
  unexplained failure go away. *Implements:* DEP-02, AGT-06.
- **KMP-03 (MUST) Repositories declared centrally.** Repositories are declared only in
  `settings.gradle.kts` (`dependencyResolutionManagement` with `repositoriesMode` set to fail on
  project repositories, and `pluginManagement`). Private or internal repositories use content
  filtering (`exclusiveContent` or `content { includeGroup(...) }`) so that a public repository
  cannot supply an internal group name. `mavenLocal()` is not used in release builds. *Implements:*
  DEP-01, DEP-07.
- **KMP-04 (MUST) JavaScript and WebAssembly lock file.** *Multiplatform only.* The npm (or yarn)
  lock file that the Kotlin Gradle plug-in keeps for JS and wasm targets (in `kotlin-js-store/`) is
  committed, and the build is set to fail when the lock file does not match. npm packages are
  dependencies like any other (DEP-03, DEP-05). *Implements:* DEP-02.
- **KMP-05 (SHOULD) Dependency locking.** Gradle dependency locking (`gradle.lockfile`) is turned on
  for the resolved configurations, so that the exact resolved versions, including transitive ones,
  are in the repository and can be read by vulnerability scanners. *Implements:* DEP-02, DEP-05.
- **KMP-06 (MUST) Gradle wrapper verified.** The Gradle wrapper is committed with
  `distributionSha256Sum` set in `gradle-wrapper.properties`, and CI validates the wrapper jar (for
  example with the Gradle wrapper validation action). *Implements:* DEP-02, BLD-03.
- **KMP-07 (MUST) Vulnerability scan covers all targets.** The vulnerability scan covers the JVM
  dependencies and the npm dependencies of JS and wasm targets (for example OSV-Scanner on the
  Gradle and npm lock files, or the OWASP Dependency-Check Gradle plug-in). *Implements:* DEP-05.
- **KMP-08 (MUST) SBOM covers all targets.** The SBOM is produced by the build (for example with the
  CycloneDX Gradle plug-in) and includes the npm dependencies of JS and wasm targets and, for
  applications, the bundled Java runtime. *Implements:* DEP-09.

### Build

- **KMP-09 (MUST) Toolchains fixed.** The JDK version is fixed with a Gradle Java toolchain, and the
  Kotlin version with the plug-in version in the catalogue. Toolchain download, if used, comes only
  from a trusted source. *Implements:* BLD-03.
- **KMP-10 (MUST) Warnings as errors.** The Kotlin compiler option `allWarningsAsErrors` is on for
  all targets, with recorded suppressions (`@Suppress` with a comment saying why). This is stricter
  than COD-08, which allows the rule to apply to new code only. *Implements:* COD-08.
- **KMP-11 (SHOULD) Reproducible archives.** Archive tasks set `isPreserveFileTimestamps = false`
  and `isReproducibleFileOrder = true`, and build-time values (date, host, user) are not written
  into artefacts. *Implements:* BLD-08.
- **KMP-12 (MUST NOT) No secrets in Gradle files.** Credentials are not put in `gradle.properties`,
  `local.properties`, build scripts or start scripts in the repository. In CI they come from the CI
  system's protected secrets (for example as `ORG_GRADLE_PROJECT_` environment variables set by the
  CI job); on a developer computer from the user's own Gradle home or a key store, never from a file
  in the repository. *Implements:* SRC-07.
- **KMP-13 (MUST) CI runs every target.** CI runs the tests of every supported target (for example
  `jvmTest`, `jsTest`, `wasmJsTest`, native test tasks), not only the JVM. *Implements:* TST-01,
  QPL-03.

### Code

- **KMP-14 (MUST) Static analysis.** detekt (with its formatting rules or ktlint) runs in CI with a
  committed configuration and baseline (see the adoption guide), and CodeQL or an equivalent
  security analyser runs on the JVM code. *Implements:* COD-08, TST-03, QCR-01.
- **KMP-15 (MUST) Safe serialisation.** kotlinx.serialization is used with explicit types.
  Polymorphic deserialisation of untrusted data accepts only a closed set of registered subclasses
  (sealed classes or an explicit serializers module). Java serialisation (`ObjectInputStream`) is
  not used for untrusted data. *Implements:* COD-04.
- **KMP-16 (MUST) Parsers with limits.** XML parsers have external entities and DTDs turned off;
  JSON, YAML and other parsers have limits on size and depth. *Implements:* COD-10.
- **KMP-17 (MUST) Bounded coroutines.** Coroutines use structured concurrency: no `GlobalScope` for
  work started by input, timeouts on network and long-running calls, and cancellation passed on.
  *Implements:* COD-10.
- **KMP-18 (MUST) Platform code reviewed as security code.** *Multiplatform only.* `expect`/`actual`
  implementations that touch files, processes, network, cryptography or secrets are treated as
  security-relevant code (DES-06), and each platform implementation is tested. *Implements:* DES-06,
  TST-02.
- **KMP-19 (MUST) Cryptography per platform.** Cryptography uses the platform's vetted
  implementation (for example the JDK providers on the JVM, the Web Crypto API in the browser) or a
  maintained multiplatform library, never code written in the repository. *Implements:* COD-05.
- **KMP-20 (SHOULD) Coverage and API documentation in the build.** Coverage is measured with Kover
  and API documentation is generated with Dokka. *Implements:* TST-09, QDO-03.

### Release

- **KMP-22 (MUST) Desktop packages signed.** Desktop application packages (for example from Compose
  Multiplatform packaging or jpackage) are code-signed for each operating system, and notarised for
  macOS. The bundled Java runtime is a supported, patched version, and is updated when it has
  security fixes. *Implements:* APP-08, DEP-06.
- **KMP-23 (MUST) Web targets hosted safely.** JS and wasm applications served from a web server use
  a content security policy and the other headers of APP-12, and do not load scripts from other
  origins unless they are pinned with subresource integrity. This is stricter than APP-12, which is
  a SHOULD. *Implements:* APP-12, DEP-02.

## Checklist

Status: **met**, **partly**, **not met**, **n/a**. Every "not met" MUST and every "n/a" needs a
short reason; a "not met" MUST also needs an exception (GOV-05). In a public repository, the
evidence column follows GOV-09: status, public links and target dates only.

| Id | Level | Requirement | Status | Evidence or reason |
|----|-------|-------------|--------|--------------------|
| KMP-01 | MUST | Versions in one catalogue | | |
| KMP-02 | MUST | Gradle dependency verification | | |
| KMP-03 | MUST | Repositories declared centrally | | |
| KMP-04 | MUST | JavaScript and WebAssembly lock file | | |
| KMP-05 | SHOULD | Dependency locking | | |
| KMP-06 | MUST | Gradle wrapper verified | | |
| KMP-07 | MUST | Vulnerability scan covers all targets | | |
| KMP-08 | MUST | SBOM covers all targets | | |
| KMP-09 | MUST | Toolchains fixed | | |
| KMP-10 | MUST | Warnings as errors | | |
| KMP-11 | SHOULD | Reproducible archives | | |
| KMP-12 | MUST NOT | No secrets in Gradle files | | |
| KMP-13 | MUST | CI runs every target | | |
| KMP-14 | MUST | Static analysis | | |
| KMP-15 | MUST | Safe serialisation | | |
| KMP-16 | MUST | Parsers with limits | | |
| KMP-17 | MUST | Bounded coroutines | | |
| KMP-18 | MUST | Platform code reviewed as security code | | |
| KMP-19 | MUST | Cryptography per platform | | |
| KMP-20 | SHOULD | Coverage and API documentation in the build | | |
| KMP-22 | MUST | Desktop packages signed | | |
| KMP-23 | MUST | Web targets hosted safely | | |
