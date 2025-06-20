import streamlit as st
import pandas as pd
import requests

st.title("Solar Inverter Energy Monitoring")

WEBHOOK_URL = "https://alpino-ai.app.n8n.cloud/webhook/duka-solar-inverter"

try:
    response = requests.get(WEBHOOK_URL)
    response.raise_for_status()
    data = response.json()
except Exception as e:
    st.error(f"Error fetching data from n8n: {e}")
    st.stop()

df = pd.DataFrame(data)
df["timestamp_gmt2"] = pd.to_datetime(df["timestamp_gmt2"])
df["EP_h"] = pd.to_numeric(df["EP_h"], errors="coerce")
df = df.sort_values("timestamp_gmt2")

st.line_chart(df.set_index("timestamp_gmt2")["EP_h"])
