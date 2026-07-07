import json
import re
from app.ollama_client import ask


def extract_invoice(text: str):

    with open("app/prompts/invoice.txt") as f:
        prompt = f.read()

    prompt = prompt.replace("{{TEXT}}", text)

    response = ask(prompt)

    # rimuove eventuali blocchi markdown ```json ... ```
    response = re.sub(r"```(?:json)?", "", response)
    response = response.replace("```", "").strip()

    try:
        return json.loads(response)
    except Exception:
        return {
            "error": "Invalid JSON from model",
            "raw": response
        }
