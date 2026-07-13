DOCUMENT_CHECK_PROMPT = """
You are an expert Letter of Credit document checker.

Analyze the following documents and verify their consistency.

LETTER OF CREDIT:
{lc}

COMMERCIAL INVOICE:
{invoice}

AIR WAYBILL:
{awb}

INSURANCE CERTIFICATE:
{insurance}

Check:
- seller and buyer names
- quantities
- amounts
- currencies
- incoterms
- shipment dates
- ports/airports
- insurance coverage
- required documents

Return ONLY valid JSON.

Use this format:

{{
    "status": "OK|WARNING|DISCREPANCY",
    "summary": "",
    "checks": [
        {{
            "field": "",
            "result": "OK|ERROR",
            "note": ""
        }}
    ],
    "missing_documents": [],
    "remarks": []
}}
"""