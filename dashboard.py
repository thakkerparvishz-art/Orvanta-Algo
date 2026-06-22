import streamlit as st
import pandas as pd
import datetime

# --- Page Configuration ---
st.set_page_config(page_title="Orvanta Algo Dashboard", layout="wide")

# --- Header ---
st.title("🚀 Orvanta Algo Trading Dashboard")

# --- Sidebar: Authentication ---
st.sidebar.header("Client Login")
user_id = st.sidebar.text_input("User ID")
password = st.sidebar.text_input("Password", type="password")

if st.sidebar.button("Login"):
    st.sidebar.success(f"Welcome, {user_id}!")

st.sidebar.markdown("---")

# --- Sidebar: Strategy Selection ---
st.sidebar.header("Strategy Selection")
strategies = ["Short Straddle", "Iron Condor", "Ratio Spread"]
selected_strategy = st.sidebar.selectbox("Choose a Strategy", strategies)

if st.sidebar.button("Activate Strategy"):
    st.sidebar.write(f"Executing {selected_strategy}...")

# --- Main Dashboard Area ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("System Status")
    status_data = {
        "Metric": ["WebSocket", "Latency", "Compliance"],
        "Value": ["Connected", "12ms", "9-Lot Limit"]
    }
    st.table(pd.DataFrame(status_data))

with col2:
    st.subheader("Live Market")
    st.write(f"System Time: {datetime.datetime.now().strftime('%H:%M:%S')}")
    st.info("System Mode: TRADING ENABLED")
