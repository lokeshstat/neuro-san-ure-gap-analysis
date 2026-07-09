# URE Gap Analysis System

Public project scaffold using neuro-san-project-example layout, with one generated network wired in.

## Structure
- backend/: network runtime + registries
- frontend/: Streamlit entrypoint
- backend/registries/my_agent.hocon: generated network config

## Run
1. Create virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Configure API keys (if required by your chosen LLM config)
4. Start UI: `streamlit run frontend/run.py`
