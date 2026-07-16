import json

from core.ollama_client import ask
from .prompts import LC_ANALYSIS_PROMPT
from .parser import parse_lc


def analyze_lc(lc):

    # estrazione campi LC
    fields = parse_lc(lc)

    field46a = fields.get("46A", "")
    field47a = fields.get("47A", "")

    prompt = LC_ANALYSIS_PROMPT.format(
        field46a=field46a,
        field47a=field47a
    )

    response = ask(prompt)

    response = response.strip()

    response = response.strip()

    # elimina eventuali blocchi markdown
    response = response.replace("```json", "")
    response = response.replace("```", "")

    # prende solo la parte JSON
    start_obj = response.find("{")
    start_arr = response.find("[")

    if start_obj == -1 or (start_arr != -1 and start_arr < start_obj):
        start = start_arr
    else:
        start = start_obj

    if start != -1:
        response = response[start:]

    response = response.strip()


    try:
        return json.loads(response)

    except json.JSONDecodeError:
        return {
            "status": "ERROR",
            "raw_response": response
        }