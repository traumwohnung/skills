# Testing Strategy: <system>

## Decision

State the assurance goal, the highest risks, and the portfolio chosen to address them. Define what “ready” means and what remains outside the claim.

Default objective: maximize distinct failure modes detected per unit of execution time and maintenance cost, subject to complete coverage of declared critical obligations.

## Scope and system model

### In scope

- Public journeys and operations:
- Components and owners:
- Processes and transports:
- Durable stores and side effects:
- Providers and external systems:
- Trust and tenant boundaries:
- Supported deployment environments:

### Out of scope

Name exclusions and who owns their evidence.

### Meaningful ends

Name each component, contract, durability, trust, workflow, and deployment slice that matters. Explain why the selected boundary can observe the claim.

## Research basis and engineering judgments

Link primary sources for empirical claims. Separate findings, limitations, and project-specific decisions. Do not present a pyramid or fixed test ratio as a universal law.

## Risk and invariant model

Rank impact, likelihood, uncertainty, and escape cost. Define safety, liveness, security, durability, compatibility, and resource-bound invariants as observable statements.

Maintain the detailed obligations in `evidence-matrix.csv`.

### Bounded coverage contract

Name every finite denominator for which the project requires 100% coverage: operations, contracts, boundaries, invariants, model transitions, failure classes, migrations, authorization rules, real-store persistence paths, viable critical mutants, or another declared set.

Explicitly exclude unbounded claims over all inputs, timings, schedules, network behavior, simultaneous failures, future dependencies, and production states.

## Current evidence

Inventory existing tests, exact commands, fixtures, CI lanes, environments, production checks, observed failures, and retained artifacts. Distinguish measured evidence from assumptions.

## Evidence portfolio

For each selected technique, state:

- obligation addressed;
- independent oracle;
- real versus substituted dependencies;
- why a cheaper layer is insufficient;
- cadence and runtime budget;
- retained failure artifacts.

Explain intentional overlap where techniques have independent failure-detection power.

## Cross-component and end-to-end slices

Define each slice’s entry point, real components, controlled doubles, state setup, public outcome, internal durable oracle, cleanup, and failure diagnosis. Keep a thin full-chain suite over shipped artifacts.

Include subsection E2Es for every high-risk ownership, durability, or trust boundary. Keep only representative cross-cutting deployment truths in the complete end-to-end suite.

## Failure and recovery model

Maintain named fault points in `failure-model.csv`. Cover crashes, network faults, storage faults, dependency refusal, malformed input, credentials, capacity, clocks, concurrency, and operator workflows where relevant.

For each case assert:

- required safety during failure;
- forbidden side effects;
- eventual liveness and deadline;
- retry/replay behavior;
- observable recovery signal.

## Test data and environments

Define factories, generated data, privacy rules, seeds, shrinking, time control, isolation, realistic scale, provider sandboxes, topology, and reproducibility. State known fidelity gaps.

## CI, release, and production lanes

| Lane | Trigger | Evidence | Budget | Required? | Artifacts and owner |
|---|---|---|---|---|---|
| Local | change | | | | |
| Pull request | change | | | | |
| Main | merge | | | | |
| Nightly | schedule | | | | |
| Release candidate | release | | | | |
| Canary | deploy | | | | |
| Production | continuous | | | | |

Define timeout, cancellation, retry, quarantine, and secret-redaction policy. A required skipped test is a failure.

## Measurable gates

Use finite denominators such as invariant, operation, state-transition, mutant, interaction, fault-point, adapter, environment, and escaped-defect coverage. Record exclusions and residual viable mutants. Treat line/branch coverage as gap-finding telemetry.

## Load, stress, soak, and recovery drills

State workload model, dataset, topology, duration, percentiles, resource budgets, correctness oracle, saturation signals, recovery target, and exact command for each experiment.

## Flake management

Capture the first failure, seed, event history, logs, and environment. Quarantine only with an owner, defect, expiry, and compensating evidence. Report flake rate and time to repair; do not hide failures through retries.

## Implementation roadmap

Order work by risk reduction per cost and prerequisites. For every step name the files, commands, owner, exit gate, and evidence-matrix obligations closed.

## Residual risk and readiness decision

List untested assumptions, production-only evidence, target-hardware or live-provider dependencies, operational prerequisites, and rollback criteria. State the readiness decision without claiming that a green suite proves absence of defects.
