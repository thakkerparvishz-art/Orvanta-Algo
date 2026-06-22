import streamlit as st
import datetime

st.set_page_config(page_title="Orvanta Algo Dashboard", layout="wide")

st.title("🚀 Orvanta Algo Trading Dashboard")

# Dashboard Sidebar
st.sidebar.header("Controls")
if st.sidebar.button("🚨 EMERGENCY KILL SWITCH"):
    st.error("ALL POSITIONS CLOSED!")

# Main Status Area
status = st.empty()
if datetime.time(9, 16) <= datetime.datetime.now().time() <= datetime.time(15, 15):
    status.success("System Status: TRADING ACTIVE")
else:
    status.warning("System Status: MARKET CLOSED")

# Strategy Table
st.subheader("Active Strategies")
st.table({
    "Strategy": ["Short Straddle", "Iron Condor", "Ratio Put Spread"],
    "Lots": [5, 2, 9],
    "Status": ["Running", "Running", "Inactive"]
})
