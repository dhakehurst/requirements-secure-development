# A1 Kotlin Multiplatform and Gradle Annex

Part of the Secure Development Requirements for Libraries, version 0.7 (draft), 2026-11-25. Read the
[README](README.md) first: it gives the wording rules, the working model, the terms and the sources.

## Scope

Applies to repositories written in Kotlin Multiplatform (JVM, JavaScript, WebAssembly, Native) and
built with Gradle. It adds no requirements: the first part says how the requirements of document 01
are met, and the second part says how the guidance of document 02 is applied. KMP-22 and KMP-23 are
used only in the set for applications. There is no separate checklist: the checklist of document 01
is the only one.

Tool and plug-in names are given as examples of what is in common use. Use the current maintained
version, and check that a named option still exists in that version before relying on it.

## Practices for the Requirements

Each of these says how a requirement of document 01 is met in a Kotlin Multiplatform repository.
Where one is not followed, the requirement still has to be met another way.

- **KMP-01 Versions in one catalogue.** All dependency and plug-in versions are in the Gradle
  version catalogue (`gradle/libs.versions.toml`), as exact versions. No dynamic versions (`+`,
  `latest.release`, ranges) and no snapshot versions in release builds. *Implements:* DEP-02.
- **KMP-02 Gradle dependency verification.** `gradle/verification-metadata.xml` is committed, with
  SHA-256 checksums (and PGP keys where the publisher signs) for every artefact, including plug-ins
  and their dependencies. The build fails on a missing or wrong checksum. Updating the file is part
  of the same reviewed change that updates the dependency, and is never done to make an unexplained
  failure go away. *Implements:* DEP-02, AGT-06.
- **KMP-03 Repositories declared centrally.** Repositories are declared only in
  `settings.gradle.kts` (`dependencyResolutionManagement` with `repositoriesMode` set to fail on
  project repositories, and `pluginManagement`). Private or internal repositories use content
  filtering (`exclusiveContent` or `content { includeGroup(...) }`) so that a public repository
  cannot supply an internal group name. `mavenLocal()` is not used in release builds. *Implements:*
  DEP-01.
- **KMP-04 JavaScript and WebAssembly lock file.** The npm (or yarn) lock file that the Kotlin
  Gradle plug-in keeps for JS and wasm targets (in `kotlin-js-store/`) is committed, and the build
  is set to fail when the lock file does not match. npm packages are dependencies like any other
  (DEP-03, DEP-05). *Implements:* DEP-02.
- **KMP-06 Gradle wrapper verified.** The Gradle wrapper is committed with `distributionSha256Sum`
  set in `gradle-wrapper.properties`, and CI validates the wrapper jar (for example with the Gradle
  wrapper validation action). *Implements:* DEP-02, LIB-16.
- **KMP-07 Vulnerability scan covers all targets.** The vulnerability scan covers the JVM
  dependencies and the npm dependencies of JS and wasm targets (for example OSV-Scanner on the
  Gradle and npm lock files, or the OWASP Dependency-Check Gradle plug-in). *Implements:* DEP-05.
- **KMP-08 SBOM covers all targets.** The SBOM is produced by the build (for example with the
  CycloneDX Gradle plug-in) and includes the npm dependencies of JS and wasm targets and, for
  applications, the bundled Java runtime. *Implements:* DEP-09.
- **KMP-12 No secrets in Gradle files.** Credentials are not put in `gradle.properties`,
  `local.properties`, build scripts or start scripts in the repository. In CI they come from the CI
  system's protected secrets (for example as `ORG_GRADLE_PROJECT_` environment variables set by the
  CI job); on a developer computer from the user's own Gradle home or a key store, never from a file
  in the repository. *Implements:* SRC-07.
- **KMP-13 CI runs every target.** CI runs the tests of every supported target (for example
  `jvmTest`, `jsTest`, `wasmJsTest`, native test tasks), not only the JVM. *Implements:* TST-01.
- **KMP-21 Maven Central publishing.** Libraries are published to Maven Central from CI only, signed
  with the Gradle signing plug-in using an in-memory key from CI secrets, with sources and
  documentation jars, complete POM metadata (licence, source repository, developers) and Gradle
  module metadata. *Implements:* LIB-01, BLD-06, DEP-08.

## Guidance

These are not requirements. They say how the guidance of document 02 is applied in a Kotlin
Multiplatform repository, and agents follow them unless there is a reason not to.

- **KMP-05 Dependency locking.** Gradle dependency locking (`gradle.lockfile`) is turned on for the
  resolved configurations, so that the exact resolved versions, including transitive ones, are in
  the repository and can be read by vulnerability scanners. *Guidance:* document 02, section 6.
- **KMP-09 Toolchains fixed.** The JDK version is fixed with a Gradle Java toolchain, and the Kotlin
  version with the plug-in version in the catalogue. Toolchain download, if used, comes only from a
  trusted source. *Guidance:* document 02, section 8.
- **KMP-10 Warnings as errors.** The Kotlin compiler option `allWarningsAsErrors` is on for all
  targets, with recorded suppressions (`@Suppress` with a comment saying why). *Guidance:* document
  02, section 5.
- **KMP-11 Reproducible archives.** Archive tasks set `isPreserveFileTimestamps = false` and
  `isReproducibleFileOrder = true`, and build-time values (date, host, user) are not written into
  artefacts. *Guidance:* document 02, section 8.
- **KMP-14 Static analysis.** detekt (with its formatting rules or ktlint) runs in CI with a
  committed configuration and baseline (see the adoption guide), and CodeQL or an equivalent
  security analyser runs on the JVM code. *Guidance:* document 02, section 3, 5.
- **KMP-15 Safe serialisation.** kotlinx.serialization is used with explicit types. Polymorphic
  deserialisation of untrusted data accepts only a closed set of registered subclasses (sealed
  classes or an explicit serializers module). Java serialisation (`ObjectInputStream`) is not used
  for untrusted data. *Guidance:* document 02, section 5.
- **KMP-16 Parsers with limits.** XML parsers have external entities and DTDs turned off; JSON, YAML
  and other parsers have limits on size and depth. *Guidance:* document 02, section 4, 5.
- **KMP-17 Bounded coroutines.** Coroutines use structured concurrency: no `GlobalScope` for work
  started by input, timeouts on network and long-running calls, and cancellation passed on.
  *Guidance:* document 02, section 5.
- **KMP-18 Platform code reviewed as security code.** `expect`/`actual` implementations that touch
  files, processes, network, cryptography or secrets are treated as security-relevant code (document
  02, section 4), and each platform implementation is tested. *Guidance:* document 02, section 4.
- **KMP-19 Cryptography per platform.** Cryptography uses the platform's vetted implementation (for
  example the JDK providers on the JVM, the Web Crypto API in the browser) or a maintained
  multiplatform library, never code written in the repository. *Guidance:* document 02, section 5.
- **KMP-20 Coverage and API documentation in the build.** Coverage is measured with Kover and API
  documentation is generated with Dokka. *Guidance:* document 02, section 7, 12.
