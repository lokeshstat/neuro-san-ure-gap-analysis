# URE Gap Analysis NeuroSAN

## Project Overview
Rule-engine referrals often include avoidable false positives, creating unnecessary manual underwriting load and missed straight-through opportunities.

## Solution Description
A grounded analysis pipeline that maps observed case outcomes to rule behavior, identifies referral gaps, and outputs recommendation-ready analytics with auditable evidence.

## Setup Instructions
1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:
   `pip install -r requirements.txt`
4. Configure required API keys/environment variables for your selected LLM/tool setup.

## How To Run The Solution
1. Optional validation: ensure backend registry files are valid HOCON.
2. Run backend (headless check):
   `python backend/run.py`
3. Run frontend:
   `streamlit run frontend/run.py`
4. Open the URL shown by Streamlit and submit inquiries.

## NeuroSAN Usage Explanation
- Network entrypoint: `backend/registries/my_agent.hocon`
- Active manifest: `backend/registries/manifest.hocon`
- Shared orchestration primitives: `backend/registries/aaosa.hocon`
- LLM/model setup: `backend/registries/llm_config.hocon`
- Custom coded tools live in `backend/coded_tools`.

## Repository Structure
```
.
├── .gitignore
├── LICENSE
├── README.md
├── architecture.md
├── requirements.txt
├── summary.md
├── backend/
│   ├── run.py
│   ├── coded_tools/
│   │   ├── __init__.py
│   │   └── my_agent/
│   │       ├── __init__.py
│   │       └── save_output.py
│   └── registries/
│       ├── aaosa.hocon
│       ├── llm_config.hocon
│       ├── manifest.hocon
│       └── my_agent.hocon
└── frontend/
    └── run.py
```

## Clean Repository Notes
This repository excludes temporary files, virtual environments, secrets, and unrelated artifacts to remain submission-ready.
