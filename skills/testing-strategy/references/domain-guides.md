# Domain Guides

Read only the sections present in the target system. These are prompts for deriving project-specific obligations, not generic acceptance checklists.

## Contents

- [HTTP and service APIs](#http-and-service-apis)
- [Durable and distributed systems](#durable-and-distributed-systems)
- [Data pipelines and projections](#data-pipelines-and-projections)
- [Security, identity, and privacy](#security-identity-and-privacy)
- [User interfaces and clients](#user-interfaces-and-clients)
- [Background jobs and schedulers](#background-jobs-and-schedulers)
- [Command-line tools and libraries](#command-line-tools-and-libraries)
- [Numerical and data-intensive software](#numerical-and-data-intensive-software)

## HTTP and service APIs

Model:

- operation, method, route, version, content type, and transport;
- authenticated identity, tenant, role, resource owner, and policy decision;
- request limits, pagination, sorting, filtering, conditional requests, and idempotency;
- downstream timeout, cancellation, retry, and partial dependency failure;
- response schema, status, headers, error taxonomy, and observability.

Use local tests for validation and policy functions, real-server component tests for middleware and serialization, consumer/provider contract suites for independently released clients, and a thin deployed slice for TLS/proxy/configuration/routing. Generate malformed and boundary inputs. Verify that invalid or unauthorized requests produce no side effects and leak no protected distinctions.

## Durable and distributed systems

Write safety and liveness separately. Typical obligations include atomic visibility, monotonic checkpoints, idempotent replay, bounded duplication, convergence, fencing stale actors, snapshot consistency, retention, backup/restore, and schema compatibility.

Use a reference state machine where practical. Place deterministic fault points before and after every durable transition and acknowledgement. Exercise crash/restart, delayed and duplicated messages, partitions, stale reads, clock changes, full disks, unavailable dependencies, restore, and concurrent actors. Assert the forbidden state immediately and eventual progress within a declared bound.

Run a thin real-process topology because serialization, process lifetime, connection pools, migrations, and deployment configuration are part of the system. Reserve random chaos for exploring after named deterministic cases are reliable. Retain seeds and event histories.

## Data pipelines and projections

Model source offsets or generations, transformation version, target checkpoint, ownership, rebuild path, deletion representation, and publication boundary. Define whether results are exactly once, at least once with idempotency, or eventually reconciled.

Cover:

- incremental application versus full rebuild equivalence;
- empty, duplicate, reordered, missing, and overlapping batches;
- crash between target writes and checkpoint advancement;
- schema and transformation upgrades;
- tombstones and resurrection;
- source retention gaps and bounded catch-up;
- backpressure, poison records, quarantine, and retry exhaustion;
- consistent publication so readers never see a half generation;
- reconciliation against the source of truth.

Use property/state-machine tests for sequences, real-database tests for atomicity, contract tests at event boundaries, and a slice E2E from source emission through consumer-visible query. Compare incremental output with an independently computed rebuild oracle over generated histories.

## Security, identity, and privacy

Build an actor × operation × resource × tenant × state matrix. Test allowed and denied cases, but prioritize denied and ambiguous states: missing, expired, revoked, wrong audience, wrong tenant, stale policy, malformed credentials, and dependency failure.

Assert authorization at the object and field level. Verify tenant isolation, secret redaction, audit completeness, cache partitioning, rate limiting, safe defaults, key rotation, and fail-closed behavior. Run hostile-input tooling at parsers and protocol edges. Use production-like middleware and identities in at least one deployed slice; bypassing auth in tests cannot establish the shipped security claim.

For cryptographic code, test official vectors, malformed inputs, version negotiation, nonce/key lifecycle, and independent interoperability. Do not invent cryptographic primitives or treat round-trip-only tests as sufficient.

## User interfaces and clients

Put formatting, reducers, validation, and state transitions below the rendered layer. Test components with accessibility roles and user-observable behavior rather than implementation selectors. Cover loading, empty, partial, stale, offline, retry, conflict, permission, and error states.

Use contract tests against recorded or generated protocol fixtures, a small number of real-backend workflow slices, and a thinner browser/device matrix selected from supported environments. Add visual regression only for intentional visual contracts and require semantic review of baseline changes. Verify keyboard navigation, focus, accessible names, reduced motion, localization expansion, time zones, and slow networks where applicable.

## Background jobs and schedulers

Model acquisition, lease/fencing, retry, deduplication, checkpoint, side effect, acknowledgement, cancellation, and dead-letter behavior. Use a virtual clock and deterministic scheduler where possible.

Test overlapping runs, crash after side effect, lease expiry, clock movement, backlog growth, poison work, retry budgets, graceful shutdown, and operator replay. Assert bounded concurrency, bounded retention, idempotent effects, visible failure, and eventual recovery. Run at least one real-process test for signals, shutdown deadlines, and scheduler wiring.

## Command-line tools and libraries

For libraries, treat the public API, type/ABI promise, feature flags, supported runtimes, and error semantics as contracts. Use downstream compile/conformance fixtures where compatibility matters.

For CLIs, test parsing locally and invoke the built executable for exit codes, stdout/stderr separation, signals, filesystem effects, locale, pipes, TTY/non-TTY behavior, and corrupt configuration. Golden output is appropriate for stable machine-readable formats; semantic assertions are preferable for prose diagnostics.

## Numerical and data-intensive software

Define accepted error bounds, units, missing-value behavior, determinism, ordering, overflow, and stability. Use analytically solvable cases, independent high-precision references, metamorphic relations, conservation laws, and differential implementations.

Generate boundary distributions rather than only uniform random values. Cover extreme magnitudes, cancellation, NaN/infinity, sparse/dense shapes, empty inputs, duplicates, ordering, and platform variation. Performance tests must also assert output validity; a fast wrong result is not a pass.
