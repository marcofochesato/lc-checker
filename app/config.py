from dotenv import load_dotenv
import os

load_dotenv()

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434/api/generate",
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.1:8b",
)
