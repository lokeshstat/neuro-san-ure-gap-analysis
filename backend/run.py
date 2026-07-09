from __future__ import annotations

import os
from pathlib import Path


def invoke_agent(inquiry: str) -> str:
    # Minimal placeholder entrypoint. Replace with actual neuro-san runner wiring as needed.
    cfg = Path(__file__).parent / "registries" / "my_agent.hocon"
    return f"Loaded config: {cfg}\nInquiry: {inquiry}"


if __name__ == "__main__":
    test_prompt = os.getenv("TEST_PROMPT", "Run a quick smoke test.")
    print(invoke_agent(test_prompt))
