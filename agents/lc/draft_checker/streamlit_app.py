import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.append(str(ROOT))

from agents.lc.draft_checker.checker import check_lc_draft

import streamlit as st
from agents.lc.draft_checker.checker import check_lc_draft


st.set_page_config(
    page_title="LC Draft Checker",
    layout="wide"
)

st.title("📄 LC Draft Checker")

st.write(
    "Inserisci il testo della Draft LC e dell'ordine "
    "per verificare la congruenza."
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Draft LC")

    lc_text = st.text_area(
        "Testo LC",
        height=400
    )

with col2:
    st.subheader("Ordine")

    order_text = st.text_area(
        "Testo ordine",
        height=400
    )


if st.button("🔍 Analizza LC"):

    if not lc_text or not order_text:
        st.warning("Inserisci sia la LC che l'ordine.")

    else:
        with st.spinner("Analisi LC in corso..."):

            result = check_lc_draft(
                lc_text,
                order_text
            )

        st.json(result)