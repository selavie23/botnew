import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import time

st.set_page_config(page_title="Cyberpunk Bot", layout="wide")

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0a0a0f 0%, #1a0b2e 100%);
    }
    h1 {
        color: #00ffff;
        text-shadow: 0 0 10px #00ffff;
    }
</style>
""", unsafe_allow_html=True)

st.title("🌌 NEURAL TRADING TERMINAL")
st.markdown("---")
st.info("Бот запущен и работает!")

# Простая статистика
col1, col2, col3 = st.columns(3)
col1.metric("Status", "Online")
col2.metric("Trades", "0")
col3.metric("Profit", "$0.00")

st.markdown("---")
st.caption(f"Updated: {datetime.now().strftime('%H:%M:%S')}")
