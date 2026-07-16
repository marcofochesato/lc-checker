import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.append(str(ROOT))

from agents.lc.document_checker.parser import parse_lc


with open("lc.txt", "r") as f:
    text = f.read()


fields = parse_lc(text)


print("46A:")
print(fields.get("46A"))

print("\n47A:")
print(fields.get("47A"))