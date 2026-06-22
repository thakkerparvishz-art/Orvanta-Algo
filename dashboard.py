import streamlit as st
import pandas as pd
import datetime

# --- Page Configuration ---
st.set_page_config(page_title="Orvanta Algo Dashboard", layout="wide")

# --- Header ---
st.title("🚀 Orvanta Algo Trading Dashboard")
st.markdown("---")

# --- Sidebar Controls ---
st.sidebar.header("System Controls")
if st.sidebar.button("🚨 EMERGENCY KILL SWITCH", type="primary"):
    st.sidebar.error("KILL COMMAND SENT: All positions flattening...")
    # Add your broker API call logic here

st.sidebar.markdown("---")
st.sidebar.info("Market Status: " + ("LIVE" if 9 <= datetime.datetime.now().hour < 16 else "CLOSED"))

# --- Main Dashboard Area ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Active Strategies")
    # Mock data for demonstration - replace with your actual API data
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
    st.write("Last Sync: " + datetime.datetime.now().strftime("%H:%M:%S"))

# --- Footer/Logs ---
st.markdown("### Recent Audit Logs")
st.text("09:16:01 - Strategy 1 Initialized")
st.text("09:16:05 - WebSocket Feed Locked")
