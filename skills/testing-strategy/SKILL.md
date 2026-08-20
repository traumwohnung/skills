---
name: testing-strategy
description: Design, audit, implement, and validate research-grounded software testing strategies that maximize independent fault-detection power per test. Use for test plans, quality strategies, production-readiness assurance, component versus integration/E2E boundaries, coverage goals, invariant and failure matrices, property/model/mutation/combinatorial testing, CI test lanes, flaky-suite repair, resilience/load/soak testing, or deciding what evidence a software change needs.
---

# Testing Strategy

Maximize distinct failure modes detected per unit of execution time and maintenance cost. Build confidence from explicit risks, invariants, and independent oracles. Treat test count and code coverage as diagnostics, never as proof of quality.

## Route the task

Choose the requested outcome before acting:

- **Explain:** teach the strategy and distinguish research findings from engineering judgment.
- **Audit:** inspect the repository and report evidence, gaps, duplication, and unsupported claims without changing files.
- **Design:** produce a testing strategy, invariant/evidence matrix, failure model, and staged roadmap.
- **Implement:** add the smallest high-value tests and CI gates, run them, and leave reproducible evidence.
- **Production assurance:** combine pre-release tests with migrations, restore drills, load/soak, canary, observability, and rollback criteria.

For audit or implementation, read repository instructions first. Inventory source contracts, components, state stores, trust boundaries, deployment artifacts, test suites, CI, and existing failures before recommending new tools.

For design, implementation, or production-assurance work, read [hands-on-playbook.md](references/hands-on-playbook.md). Use its recipes to produce executable tests, exact commands, named fault points, CI jobs, and retained evidence—not only a theoretical strategy.

## Apply research responsibly

Read [research-evidence.md](references/research-evidence.md) whenever making claims about test effectiveness, coverage, mutation, generated testing, combinatorial testing, formal methods, flakiness, regression selection, or distributed fault injection.

Use these rules:

1. Prefer primary peer-reviewed work, official standards, and original system papers.
2. State the studied population and limitation when translating a finding into practice.
3. Label project-specific choices as judgments, not scientific laws.
4. Treat pyramids, trophies, and fixed unit/integration/E2E ratios as heuristics, not evidence-backed universal targets.
5. Never claim that passing tests prove absence of defects in the open world. Scope every completeness claim to a finite contract, model, mutation set, or interaction space.
6. Browse for current research or standards when the user requests citations, regulated-domain guidance, or up-to-date recommendations. Link the primary source nearest the supported claim.

## Build the system model

Map the application before selecting tests:

1. List externally visible journeys and public operations.
2. Draw component, process, transport, database, provider, queue, and trust boundaries.
3. Identify durable state, side effects, ownership, consistency promises, and recovery paths.
4. Record supported runtimes, databases, providers, deployment shapes, and compatibility promises.
5. Identify uncertainty: novel algorithms, poorly understood dependencies, concurrency, security, migrations, and historical escapes.

Define meaningful “ends” relative to risk. Test adjacent slices at durable or trust boundaries for diagnosis, plus a thin full customer chain for assembly. Do not force every scenario through the longest chain.

## Derive obligations before examples

Express each critical requirement as an observable invariant. Cover at least:

- safety and atomic visibility;
- durability and restore;
- idempotency, replay, ordering, and monotonic progress;
- convergence after transient failure;
- authorization, privacy, and fail-closed behavior;
- bounded time, bytes, memory, retries, queues, and work;
- compatibility and migration;
- availability, readiness, degradation, and recovery observability.

For every obligation define:

- positive example;
- counterexample or forbidden outcome;
- independent oracle;
- fault/timing point;
- lowest sufficient test layer;
- deployed slice if wiring is part of the claim;
- cadence, owner, and retained evidence.

Start from [evidence-matrix.csv](assets/evidence-matrix.csv) when a durable matrix helps. Validate it with:

```sh
python3 scripts/validate_evidence_matrix.py path/to/evidence-matrix.csv --require-rows
```

## Select an evidence portfolio

Place each claim at the lowest layer that can observe it without mocking the subject of the assertion. Read [technique-selection.md](references/technique-selection.md) for detailed selection rules.

- Use **example/unit tests** for local rules, boundaries, parsing, and precise errors.
- Use **property-based tests** for algebraic laws, state transitions, replay, serialization, and broad generated inputs.
- Use **metamorphic or differential tests** when exact expected outputs are costly but relations or independent implementations exist.
- Use **fuzzing** for parser, protocol, and hostile-input robustness.
- Use **mutation testing** selectively to test assertion sensitivity in critical logic.
- Use **real-adapter integration tests** for transactions, migrations, databases, crypto, filesystems, queues, and provider adapters.
- Use **contract/conformance tests** on both producer and consumer to detect boundary and mock drift.
- Use **slice E2E tests** across each high-risk ownership, durability, or trust boundary.
- Use a **thin full-chain E2E suite** for shipped images, configuration, auth, transports, persistence, and customer-visible outcomes.
- Use **model checking or model-based testing** for bounded concurrent protocols and state machines.
- Use **deterministic simulation and named fault injection** before seeded chaos for distributed recovery.
- Use **covering arrays** for constrained interaction spaces; keep named regressions for known failures.
- Use **load, stress, and soak** for distinct hypotheses: capacity, overload behavior, and degradation over time.
- Use **canaries and production telemetry** for assumptions that hermetic testing cannot close.

Do not duplicate the same path with the same oracle merely to increase count. Preserve independent evidence types even when they cover the same lines.

## Design failures systematically

For every state-changing operation inject failure:

1. before the side effect;
2. after the side effect but before durable acknowledgement;
3. during durable commit;
4. after commit but before the response;
5. during retry, replay, or competing execution.

For reads, inject failure before authorization, during dependency access, between pages/chunks, and after credentials, epochs, snapshots, or pins change.

Cover process crash/pause, network loss/latency/reset/truncation/reorder/duplicate, storage loss/stale write/restore, dependency refusal, malformed input, credential states, capacity boundaries, clock movement, and operator workflows. Assert both required state and forbidden side effects.

Start from [failure-model.csv](assets/failure-model.csv) for distributed or durable systems. Read [domain-guides.md](references/domain-guides.md) only for the domains present in the target application.

## Optimize for confidence per cost

Rank gaps using:

```text
priority ≈ impact × likelihood × uncertainty × escape_cost / implementation_and_runtime_cost
```

Use the expression for discussion, not fake precision. Prioritize catastrophic invariants even when likelihood is uncertain.

Reduce cost by moving exhaustive cases downward, keeping deployed tests thin, using constrained covering arrays, and prioritizing tests that historically detect failures early. Apply change-based selection only when dependency analysis is trustworthy and a required full lane still runs. Do not minimize solely by shared code coverage; empirical work shows that equal structural coverage can retain different fault-detection power.

## Define honest coverage and gates

Use finite, auditable claims such as:

- every declared API operation is exercised;
- every producer/consumer contract is tested on both sides;
- every architectural ownership, durability, and trust boundary has a suitable slice;
- every declared public operation is auth-gated and functionally invoked;
- every named invariant has an executable or formal oracle;
- every reachable state in a bounded model is checked;
- every catalogued critical failure class is injected at its named points;
- every supported migration and upgrade path is exercised;
- every authorization rule has allowed and denied evidence;
- every persistence operation with semantic importance runs against its real store;
- no viable critical-path mutant survives;
- every valid `t`-way interaction in the declared factor model is covered;
- every escaped defect has a stable regression;
- every supported production adapter runs its contract suite.

Do not write “100% tested” without naming the finite denominator. Never claim exhaustive coverage of all inputs, timings, schedules, network behaviors, simultaneous failures, future dependency behavior, or production infrastructure states.

Define local, pull-request, main, nightly, release-candidate, canary, and production lanes. A skipped required test is not green. Retries may diagnose flakes but must not rewrite the first failure into success. Quarantine requires an owner, defect, expiry, and compensating evidence.

## Implement in value order

When authorized to change code:

1. Add or strengthen the cheapest independent oracle for the highest risk.
2. Prove the regression fails against the defect when practical.
3. Add real-adapter coverage for durability or boundary claims.
4. Add one deployed slice only when configuration/process/transport matters.
5. Add the failure at deterministic timing points.
6. Add CI cadence, timeouts, artifacts, and secret redaction.
7. Run focused tests, then the affected portfolio, then the required release lane.
8. Update the evidence matrix and strategy document with actual commands and limits.

Use [strategy-template.md](assets/strategy-template.md) when creating a new strategy document. Adapt it; remove irrelevant sections rather than filling them with generic prose.

## Validate the strategy

Before handing off, verify:

- each critical invariant has a positive and negative oracle;
- no mock replaces the behavior being asserted;
- expected values are independent of the production helper under test;
- every public boundary has contract and authorization evidence;
- every durable commit has crash, replay, and competing-writer evidence;
- generated and chaos failures retain seeds and minimal counterexamples;
- timeouts, pages, bytes, retries, and resource budgets are explicit;
- logs and artifacts are bounded and secret-safe;
- liveness and readiness are not conflated;
- full-chain tests use shipped artifacts and production-like topology;
- limitations, untested assumptions, and production-only evidence are explicit.

Report observed evidence separately from proposed work. Never call a system production-ready solely because the suite is green; state what remains dependent on target hardware, live providers, staged rollout, operational telemetry, and incident response.

## Required deliverable shape

Lead with the decision and top risks. Then provide:

1. system and boundary model;
2. current evidence and gaps;
3. invariant/evidence matrix;
4. selected portfolio and why each layer is independent;
5. failure and interaction model;
6. implementation sequence by value and prerequisite;
7. CI/release/production lanes;
8. measurable gates and exact commands;
9. limitations and residual risk.

Keep recommendations concrete enough to implement. Name files, test targets, fault points, or contracts discovered in the repository instead of returning a generic checklist.
