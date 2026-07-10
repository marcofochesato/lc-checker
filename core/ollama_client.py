import requests
from core.config import OLLAMA_URL, OLLAMA_MODEL


def ask(prompt: str) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
        },
        timeout=300,
    )

    response.raise_for_status()
    return response.json()["response"]
