# Swift Review Pack

## Project pitch

A lightweight local coding agent harness for repository-grounded engineering tasks. It wraps a model with workspace context, explicit tools, state tracking, memory, run artifacts, and benchmark evidence.

## Architecture map

- `swift.cli` wires configuration, provider clients, workspace context, and the runtime.
- `swift.runtime.Swift` coordinates the agent control surface.
- `swift.context_manager` builds bounded model context from prefix, memory, history, and the current request.
- `swift.tools` defines the explicit tool allowlist used by the runtime.
- `swift.run_store` writes per-run artifacts for review and replay.

## Benchmark evidence

Benchmark runs should preserve reproducibility metadata, task rows, summary counts, and failure categories so reviewers can distinguish runtime regressions from task or provider failures.

## Sample run artifact list

- `.swift/runs/<run_id>/task_state.json`
- `.swift/runs/<run_id>/trace.jsonl`
- `.swift/runs/<run_id>/report.json`
