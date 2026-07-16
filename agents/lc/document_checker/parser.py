import re


LC_FIELDS = [
    "20",
    "31C",
    "31D",
    "32B",
    "39A",
    "41D",
    "42C",
    "43P",
    "43T",
    "44E",
    "44F",
    "45A",
    "46A",
    "47A",
    "48",
]


def parse_lc(text):

    fields = {}

    for field in LC_FIELDS:

        pattern = rf":{field}:([\s\S]*?)(?=\n:[0-9A-Z]{{2,3}}:|$)"

        match = re.search(pattern, text)

        if match:
            fields[field] = match.group(1).strip()

    return fields