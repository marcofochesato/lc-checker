import json

from core.ollama_client import ask
from .prompts import DOCUMENT_CHECK_PROMPT


def check_documents(
    lc,
    invoice,
    awb,
    insurance
):
    prompt = DOCUMENT_CHECK_PROMPT.replace(
        "{lc}", lc
    ).replace(
        "{invoice}", invoice
    ).replace(
        "{awb}", awb
    ).replace(
        "{insurance}", insurance
    )

    response = ask(prompt)

    # pulizia eventuali ```json
    response = response.strip()

    if response.startswith("```"):
        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

    try:
        return json.loads(response)

    except Exception:
        return {
            "status": "ERROR",
            "raw_response": response
        }