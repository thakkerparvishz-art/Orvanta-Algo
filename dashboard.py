import streamlit as st
import pandas as pd
import datetime

# --- Page Configuration ---
st.set_page_config(page_title="Orvanta Algo Dashboard", layout="wide")

# --- Timing Logic ---
now = datetime.datetime.now().time()
market_open = datetime.time(9, 16)
market_close = datetime.time(15, 15)
status = "TRADING ENABLED" if market_open <= now <= market_close else "LOCKED"

# --- Header ---
st.title("🚀 Orvanta Algo Trading Dashboard")
st.markdown("---")

# --- Sidebar Controls ---
st.sidebar.header("System Controls")
st.sidebar.info(f"System Mode: {status}")

if st.sidebar.button("🚨 EMERGENCY KILL SWITCH", type="primary"):
    st.sidebar.error("KILL COMMAND SENT: All positions flattening...")

# Compliance Lot Input
lots_input = st.sidebar.number_input("Select Lots", min_value=1, max_value=9)
if lots_input > 9:
    st.sidebar.error("Compliance Error: Max 9 lots.")

st.sidebar.markdown("---")

# --- Main Dashboard Area ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Active Strategies")
    data = {
        "Strategy": ["Short Straddle", "Iron Condor", "Ratio Put Spread"],
        "Lots": [5, 2, 9],
        "Status": ["Running", "Running", "Inactive"]
    }
    df = pd.DataFrame(data)
    st.table(df)

with col2:
    st.subheader("System Health")
    st.write("WebSocket Connection: ✅ Connected")
    st.write("API Latency: 12ms")
    st.write(f"Last Sync: {datetime.datetime.now().strftime('%H:%M:%S')}")

# --- Footer/Logs ---
st.markdown("### Recent Audit Logs")
st.text("09:16:01 - Strategy 1 Initialized")
st.text("09:16:05 - WebSocket Feed Locked")
