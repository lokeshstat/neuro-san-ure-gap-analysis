# Architecture

## Overall Architecture
The solution follows a two-layer layout:
1. Frontend layer (Streamlit) in `frontend/run.py` for user interaction.
2. Backend layer in `backend/run.py` that loads and invokes the NeuroSAN network from `backend/registries/my_agent.hocon`.

## Agentic Workflow
Orchestrator routes through ingestion, rule enrichment, gap analysis, impact modeling, and stakeholder reporting with coded-tool fast paths.

The high-level execution model is:
1. Intake user inquiry.
2. Route through the configured orchestrator/agents.
3. Use coded tools where deterministic operations or persistence are required.
4. Aggregate outputs and return a user-facing response.

## Agent Interactions
- Orchestrator agent receives requests and delegates to specialized agents/tools.
- Specialized agents perform focused tasks (retrieval, analysis, evaluation, or formatting).
- Coded tools provide deterministic data handling and file persistence when required.
- The orchestrator merges outputs into a final response contract.

## Design Decisions
- Keep the repository minimal and submission-friendly using a consistent structure.
- Separate orchestration config (HOCON) from runtime code for easier change management.
- Use deterministic coded tools for operations that should not rely on LLM inference.
- Maintain a single manifest entrypoint to simplify automation and CI checks.

## NeuroSAN Components Used
- Registry and network configuration via `manifest.hocon` and `my_agent.hocon`
- AAOSA-style orchestration contract via `aaosa.hocon`
- Shared model configuration via `llm_config.hocon`
- Coded tools under `backend/coded_tools`
