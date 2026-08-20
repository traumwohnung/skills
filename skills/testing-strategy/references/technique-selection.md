# Technique Selection

Use this guide after defining risks and invariants. Select a technique because its oracle can observe a failure, not because a preferred test shape needs filling.

## Selection questions

For each obligation, ask in order:

1. What harmful outcome must be detected or prevented?
2. What observation would distinguish correct from incorrect behavior?
3. Is that oracle independent of the implementation under test?
4. Which dependencies must be real for the claim to mean anything?
5. What is the lowest-cost layer that preserves those dependencies?
6. Which fault timing, input class, state, or interaction remains uncertain?
7. Does another technique add independent detection power or merely repeat the same path?

## Technique map

| Technique | Prefer when | Strong oracle | Main limitation |
|---|---|---|---|
| Example/unit | A local rule has crisp examples and boundaries | Explicit expected value or state | Sparse examples miss input and state spaces |
| Property-based | Laws hold across many inputs or command sequences | Invariant, algebraic law, or reference model | Weak properties can pass broken implementations |
| Metamorphic | Exact answers are expensive but transformations imply relations | Relation between source and transformed runs | Metamorphic relations may also be incomplete |
| Differential | Independent implementations or versions should agree | Cross-implementation comparison | Shared defects and permitted differences need handling |
| Fuzzing | Parsers, protocols, unsafe boundaries, or hostile inputs dominate risk | Crash, sanitizer, invariant, or semantic checker | Crash-only fuzzing misses silent semantic errors |
| Mutation | You need to assess assertion sensitivity | Killed, viable, non-equivalent mutants | Equivalent mutants and runtime make broad use expensive |
| Component integration | A database, queue, filesystem, crypto library, or runtime supplies semantics | External state plus public response | Test doubles cannot establish adapter behavior |
| Contract/conformance | Independently deployed producer and consumer can drift | Shared executable protocol/schema suite | Compatibility is not full business correctness |
| Slice E2E | A durability, trust, ownership, or protocol boundary is the risk | Customer-visible outcome plus boundary state | More setup and diagnosis cost than component tests |
| Full-chain E2E | Packaging, wiring, configuration, and the whole shipped topology are the claim | Observable public outcome through deployed entry point | Slow, brittle, and poor at exhaustive combinations |
| Model-based/model checking | State machines, retries, leases, or concurrency dominate | Reference model or temporal properties | Bounded models do not prove an unbounded implementation |
| Fault injection/simulation | Recovery depends on precise failure timing | Safety and eventual-liveness invariants | Unrealistic fault models create false confidence |
| Covering arrays | Many factors interact and exhaustive combinations are infeasible | Expected result for every selected combination | `t`-way coverage is not semantic correctness |
| Load/stress/soak | Capacity, overload, or time-dependent degradation is the claim | SLO plus resource and correctness assertions | Nonrepresentative workloads produce misleading limits |
| Canary/production checks | Real infrastructure or provider behavior cannot be reproduced fully | SLOs, invariants, business probes, rollback signals | Detects exposure; it does not replace prevention |

## Decide the meaningful ends

An end-to-end test is relative to the claim. Use multiple useful ends:

- **Component end:** public API through its real stateful adapter.
- **Contract end:** producer serialization through consumer interpretation.
- **Durability end:** accepted write through restart, replay, and read-back.
- **Trust end:** untrusted request through authentication, authorization, filtering, and audit.
- **Workflow end:** public entry point through the smallest complete user outcome.
- **Deployment end:** shipped artifact, production-like configuration, network, state store, and external stub or sandbox.

Test high-risk boundaries as slices because they localize failures. Retain a thin deployment end-to-end suite because independently correct slices can still be assembled incorrectly. Do not send every edge case through the full topology.

## Choose an oracle

Prefer, in rough order:

1. externally specified expected result;
2. independent reference implementation or simple model;
3. durable state and forbidden-side-effect assertions;
4. algebraic or metamorphic relation;
5. protocol/schema conformance;
6. runtime safety signal such as sanitizer, panic, or leak detector;
7. snapshot or golden output, only when reviewed and semantically stable.

Avoid computing the expected result with the same helper or query shape used by production. Assert absence as well as presence: no duplicate side effect, no unauthorized row, no partial commit, no unbounded retry, and no secret in artifacts.

## Match technique to uncertainty

- **Input uncertainty:** partitions, property generation, fuzzing, and metamorphic relations.
- **State uncertainty:** state-machine generation, model-based testing, replay, and migration paths.
- **Interaction uncertainty:** pairwise or higher-strength covering arrays with constraints.
- **Timing uncertainty:** deterministic scheduling, virtual clocks, barriers, and named fault points.
- **Implementation uncertainty:** differential testing, mutation testing, independent reimplementation.
- **Environment uncertainty:** real adapters, deployment slices, load tests, canaries, and telemetry.
- **Human/operational uncertainty:** restore, rollback, rotation, failover, and incident drills.

## Measure coverage without confusing it for quality

Track structural coverage to locate unexercised code, not to claim correctness. Add metrics tied to finite obligations:

- requirement and invariant coverage;
- public-operation and authorization-decision coverage;
- state-transition and bounded-model coverage;
- mutation score after excluding equivalent or out-of-scope mutants;
- valid `t`-way interaction coverage;
- fault-point and recovery-path coverage;
- adapter and supported-environment coverage;
- escaped-defect regression coverage;
- SLO and resource-budget evidence under declared workloads.

When a target is 100%, name the denominator and exclusions. A critical invariant with no oracle outweighs thousands of covered lines.

## Separate performance experiments

- **Load:** prove declared throughput and latency under representative steady demand.
- **Stress:** cross the capacity boundary and assert controlled rejection, bounded queues, and recovery.
- **Spike:** apply abrupt demand changes and inspect admission control and autoscaling.
- **Soak:** hold representative load long enough to reveal leaks, compaction debt, timer drift, and backlog growth.
- **Scalability:** vary resources and demand to measure the response curve.

Every experiment needs a workload model, dataset, topology, warm-up, duration, percentile method, correctness oracle, resource budgets, and reproducible command. A latency chart without correctness and saturation signals is incomplete.

## Avoid common portfolio failures

- Do not prescribe a universal unit/integration/E2E ratio.
- Do not mock the database while claiming transaction correctness.
- Do not use snapshots as the only oracle for security or durable state.
- Do not let retries turn a first failure into a green result.
- Do not run chaos without named hypotheses and steady-state invariants.
- Do not use production traffic as the first test of recovery.
- Do not delete slower independent tests solely because faster tests cover the same lines.
- Do not require full-chain E2E for every input permutation.
- Do not confuse fault injection with fault tolerance; assert recovery and bounded harm.
