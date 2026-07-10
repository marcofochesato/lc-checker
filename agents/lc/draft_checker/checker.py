import json
from pathlib import Path

from core.ollama_client import ask


PROMPT_FILE = Path(__file__).parent / "prompts" / "draft_check.txt"


def check_lc_draft(lc_text, order_text):

    system_prompt = PROMPT_FILE.read_text()

    prompt = f"""
{system_prompt}


DRAFT LC:

----------------
{lc_text}
----------------


ORDER:

----------------
{order_text}
----------------
"""

    response = ask(prompt)

    try:
        return json.loads(response)

    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON from model",
            "raw": response
        }