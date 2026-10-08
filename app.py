from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Phishing Website Detector", page_icon="🛡️", layout="wide")

# Remove Streamlit's default padding/header so the page fills the window
st.markdown(
    """
    <style>
      header[data-testid="stHeader"] {display:none;}
      .block-container {padding:0 !important; max-width:100% !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "phishing_detector.html").read_text(encoding="utf-8")
components.html(html, height=1100, scrolling=True)
