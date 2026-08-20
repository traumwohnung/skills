# Hands-on Testing Strategy Playbook

Use this playbook to turn risks into executable evidence. Adapt names and commands to the repository; do not return the examples unchanged.

## Contents

- [Establish the coverage contract](#establish-the-coverage-contract)
- [Inventory the repository](#inventory-the-repository)
- [Build the test topology](#build-the-test-topology)
- [Design subsection end-to-end tests](#design-subsection-end-to-end-tests)
- [Keep the complete end-to-end suite thin](#keep-the-complete-end-to-end-suite-thin)
- [Turn examples into properties](#turn-examples-into-properties)
- [Build state-machine tests](#build-state-machine-tests)
- [Model critical protocols formally](#model-critical-protocols-formally)
- [Build deterministic simulation](#build-deterministic-simulation)
- [Select failure combinations](#select-failure-combinations)
- [Test the tests with mutation](#test-the-tests-with-mutation)
- [Implement CI, release, and production lanes](#implement-ci-release-and-production-lanes)
- [Finish with executable evidence](#finish-with-executable-evidence)

## Establish the coverage contract

Write the assurance objective as:

> Maximize distinct failure modes detected per unit of execution time and maintenance cost, subject to complete coverage of the declared critical obligations.

Define finite denominators before choosing percentages. Seek 100% where the set is enumerable:

- declared API operations;
- producer/consumer contracts;
- architectural ownership, durability, and trust boundaries;
- specified safety and liveness invariants;
- transitions in the declared state model;
- catalogued failure classes and named injection points;
- supported migrations, upgrades, and rollbacks;
- authorization decisions;
- semantically important persistence operations against the real store;
- critical viable mutants, after reviewing exclusions.

Explicitly reject claims of exhaustive coverage over unbounded inputs, timings, thread schedules, network behavior, simultaneous failures, future dependency behavior, and production infrastructure states. Exhaust finite spaces, model bounded spaces, generate or sample large spaces intelligently, and monitor the open world.

## Inventory the repository

Do this before proposing new tests:

1. Read repository instructions and build manifests.
2. Enumerate public entry points, schemas, migrations, state stores, queues, providers, and deployment artifacts.
3. Enumerate test files and classify them by actual dependencies—not their directory names.
4. Read CI definitions and record exact commands, triggers, timeouts, retries, services, artifacts, and skipped paths.
5. Run the cheapest discovery/list commands, then focused representative tests when authorized.
6. Map each current test to an invariant, boundary, oracle, cadence, and evidence row.
7. Report duplicated paths, mocked semantic dependencies, missing negative oracles, untested production adapters, flakes, and dead tests.

Do not infer coverage from filenames. A test called integration may mock its database; a test called unit may start a real server.

## Build the test topology

Use an assurance portfolio rather than a fixed pyramid ratio:

```text
                 production probes and reconciliation
                    thin complete user journeys
                 subsystem / slice end-to-end tests
             boundary, contract, and real-adapter tests
       model, property, mutation, fuzz, and component tests
            formal models of critical protocols when justified
```

Push exhaustive inputs and transitions down. Move upward only when process, transport, persistence, packaging, policy middleware, or deployment wiring is part of the claim.

## Design subsection end-to-end tests

Create a slice whenever a subsection owns an important invariant. Common reusable slices include:

- **External provider → ingest:** enumerate, resume, reconnect, throttle, malformed response, credential expiry, and upstream mutation. Assert eventual faithful representation without silent omission.
- **State change → event consumer:** persist, authorize, serialize/sign, deliver, retry, duplicate, revoke, and preserve cursor. Assert durable at-least-once delivery without cross-tenant leakage.
- **Canonical state → published snapshot:** construct, encrypt/sign, publish, delete, interrupt, and repeat. Assert the published snapshot is complete, internally consistent, and retrievable.
- **Service API → client SDK:** exercise every operation, response shape, scope, page, expiry, timeout, limit, malformed frame, conflict, and restart. Assert a validated result or typed failure, never ambiguous acceptance.
- **SDK → local projection → database:** rebuild, delta, delete, multi-edge catch-up, fallback, crash at each edge, duplicate, corruption, schema mismatch, and rollback. Assert data and checkpoint identify the same source version.
- **Projection/read model → public API or UI:** ordering, body retrieval, decoding, isolation, read-only policy, authentication, and recovery state. Assert exactly the state belonging to the authorized subject.

For each chosen slice record:

1. public entry and final authoritative effect;
2. real components and deliberately controlled doubles;
3. setup identity, state, clock, and data;
4. positive, forbidden, and recovery assertions;
5. fault barriers and restart method;
6. exact command, timeout, cleanup, logs, seed, and owner.

Assert the authoritative effect rather than an intermediate `200 OK`, queued message, or row count.

## Keep the complete end-to-end suite thin

Keep only cross-cutting deployment truths in the longest suite. Adapt this baseline:

1. one representative object traverses the real external protocol to the public user outcome;
2. one upstream mutation reaches visible state;
3. one restart proves durable recovery;
4. one authorization and revocation journey proves identity propagation;
5. one signed asynchronous event completes end to end;
6. one empty deployment initializes and migrates;
7. one rolling upgrade and rollback preserves declared safety and availability;
8. one backup restore reproduces the same logical state.

Use shipped artifacts and production-like topology. Do not reproduce every input and fault variation through this suite; exercise them at the narrowest slice with a valid oracle.

## Turn examples into properties

Keep one readable example for each public behavior, then express general laws. Candidate properties include:

```text
decode(encode(value)) == value
apply(snapshot, diff(snapshot, next)) == next
incremental(history) == rebuild(last_version)
apply(delta, apply(delta, state)) == apply(delta, state)
crash_before_commit preserves rows and checkpoint
crash_after_commit exposes both rows and checkpoint
unauthorized(credentials, operation, resource) == denied
scan(index) is total, stable, ordered, and duplicate-free
migrate_down(migrate_up(state)) preserves the declared reversible subset
```

Implement the smallest independent reference model practical. Generate boundary-heavy values and operation sequences, preserve seeds, shrink counterexamples, and save the minimal history as a named regression. Do not limit unit tests to happy paths; prioritize invalid states, boundaries, invariants, transitions, idempotency, determinism, error classification, and denial.

## Build state-machine tests

Use state-machine testing when failures depend on sequences rather than isolated calls.

1. Define a small model state containing only externally relevant facts.
2. Define commands with preconditions, model transitions, system calls, and postconditions.
3. Include invalid commands and competing actors where the API permits them.
4. Generate short sequences first; increase length in nightly lanes.
5. Compare every implementation result and durable checkpoint with the model after every step.
6. Inject restarts, expiry, retry, duplication, and reordered wakeups between commands.
7. Store the seed and shrunk command history on failure.

Typical machines include snapshot/lease lifecycle, projection checkpoints, retention and garbage collection, synchronization, delivery/acknowledgement, credential rotation/revocation, and provider recovery.

## Model critical protocols formally

Add a small TLA+, PlusCal, Alloy, or equivalent model when concurrency or failure schedules create a large design state space and a violated invariant would be catastrophic.

1. Model states, actions, actors, messages, durable facts, and failure assumptions above implementation detail.
2. State safety and liveness properties explicitly.
3. Bound actors, resources, queue sizes, and values; document those bounds.
4. Model-check normal operations, retry, reordering, duplication, loss, crash, recovery, and garbage collection.
5. retain the spec, configuration, exact checker command, counterexample traces, and CI cadence.
6. Translate model invariants into runtime assertions and implementation tests.
7. Review implementation-model correspondence; a checked model does not prove its implementation.

Good candidates include atomic publication/checkpoint advancement, leases and fencing, retention under pins, replication convergence, authorization-role separation, and upgrade protocols.

## Build deterministic simulation

Prefer named fault barriers and reproducible schedules before broad chaos. Introduce narrow interfaces around nondeterminism:

```text
Clock: now, sleep, advance
Entropy: next(seed)
Scheduler: spawn, yield_at(label), choose_next
Network: send, receive, delay, drop, duplicate, reorder, corrupt
Store: read, write, commit, fail, lose_ack, restart
Process: pause, crash, restart
```

Run production state-machine logic against simulated implementations where architecture permits. For each seeded scenario:

1. construct a bounded topology and workload;
2. choose operations and a named failure schedule;
3. pause at meaningful I/O and durable-transition barriers;
4. inject refusal, timeout, delay, duplication, reordering, corruption, crash, or resource exhaustion;
5. restart from simulated durable state;
6. check safety after every transition and eventual liveness within virtual time;
7. emit seed, event trace, minimal history, and state snapshot.

Run the same high-level workload against real adapters in a smaller lane. Simulation cannot establish kernel, hardware, runtime, driver, or genuine parallelism behavior.

## Select failure combinations

Avoid an uncontrolled Cartesian product:

1. Declare factors, values, invalid combinations, and expected result oracle.
2. Use pairwise coverage for ordinary configuration interactions.
3. Use three-way coverage where network, persistence, process, or credential states interact.
4. Raise strength selectively around catastrophic protocols only after measuring suite size.
5. Add explicit known-dangerous combinations regardless of generated coverage.
6. Independently verify achieved valid `t`-way coverage.

Treat pairwise and higher strengths as project-specific starting judgments, not universal empirical thresholds. If a covering-array tool is unavailable, start with an auditable factor table and targeted combinations rather than claiming coverage informally.

## Test the tests with mutation

Use mutation analysis on compact critical modules before applying it repository-wide:

1. choose authorization, validation, persistence ordering, checkpointing, signatures, timeout handling, deletion, and recovery logic;
2. run a baseline and confirm deterministic green tests;
3. generate mutants and exclude compile failures, unreachable configurations, and reviewed equivalent mutants;
4. require each meaningful mutant to be killed by a test with a discriminating oracle;
5. inspect survivors and add the smallest valuable test or document the residual risk;
6. run changed-module mutants on pull requests and a broader set nightly if runtime permits;
7. retain tool version, operators, scope, denominator, exclusions, score, and survivor report.

Do not optimize for a raw mutation percentage by adding brittle implementation assertions. Prefer behaviorally meaningful mutants and externally visible or durable oracles.

## Implement CI, release, and production lanes

Use measured runtime budgets rather than these names alone:

- **Local:** focused examples, properties, static checks, and changed tests.
- **Pull request:** unit/property/component/contract, real-store tests, critical slices, a small deterministic seed set, and changed critical mutants.
- **Main/nightly:** full-chain E2E, long state-machine sequences, large simulation campaign, broader combinations and mutation, migrations, restore, and capacity limits.
- **Release candidate:** soak, process/database fault campaign, rolling upgrade/rollback, backup restore, disk/memory pressure, credential rotation, dependency throttling/disconnection, large histories, and alert verification.
- **Canary/production:** synthetic public journey, health/readiness, SLOs, reconciliation, bounded canary exposure, automatic rollback signals, and periodic restore/recovery drills.

Measure duration, queue time, flake rate, time to repair, mutation survivors, invariant gaps, fault coverage, and escaped defects. Retry only to diagnose; preserve the first failure.

## Finish with executable evidence

Do not stop after writing a strategy when implementation is requested. Finish each selected obligation with:

- committed test or formal specification;
- demonstrated failing regression or reviewed mutation when practical;
- passing focused and portfolio commands;
- CI/release job and declared cadence;
- seed, trace, log, report, or artifact location;
- evidence-matrix row with owner and status;
- documented limitation and production-only assumption.

Call readiness only for the declared finite obligations and environments. Keep residual risks visible even when every gate passes.
