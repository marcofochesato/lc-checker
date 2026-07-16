import streamlit as st

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.append(str(ROOT))

from agents.lc.document_checker.checker import analyze_lc, analyze_lc

st.set_page_config(
    page_title="LC Document Checker",
    layout="wide"
)

st.title("📄 LC Document Checker")

st.write(
    "Inserisci i documenti in formato testo "
    "per verificare la congruenza."
)


lc_text = st.text_area(
    "Letter of Credit",
    height=250
)

invoice_text = st.text_area(
    "Commercial Invoice",
    height=250
)

awb_text = st.text_area(
    "AWB",
    height=200
)

insurance_text = st.text_area(
    "Insurance Certificate",
    height=200
)


if st.button("CHECK DOCUMENTS"):

    if not lc_text:
        st.warning("Inserire almeno la LC")
    else:
        with st.spinner("Analisi documenti in corso..."):

            # result = check_documents(
            #     lc_text,
            #     invoice_text,
            #     awb_text,
            #     insurance_text
            # )

            result = analyze_lc(lc_text)

        st.subheader("Risultato")

        st.json(result)