# pages/1_Pilot.py
import streamlit as st
from utils.data_loader import load_pilot_data
from components import header, footer, tab_info, tab_kpis, tab_dashboard


# Read pilot ID from query param
pilot_id = st.query_params.get("pilot")

if not pilot_id:
    st.error("No pilot selected.")
    st.stop()

pilot = load_pilot_data(pilot_id)

# Render header
header.render(pilot)

# Tabs
tab1, tab2, tab3 = st.tabs(["Pilot Info", "KPIs", "Dashboard"])

with tab1:
    tab_info.render(pilot["tabs"]["Pilot Info"])

with tab2:
    tab_kpis.render(pilot["tabs"]["kpis"])

with tab3:
    tab_dashboard.render(pilot["tabs"]["dashboard"])

# Render footer
footer.render(pilot["footer"])
