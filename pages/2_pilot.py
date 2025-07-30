# pages/1_Pilot.py
import streamlit as st
from streamlit import components
from utils.data_loader import load_pilot_data
from components import header, footer
from components.pilot import tab_info, tab_kpis, tab_dashboard

# Read pilot ID from query param
pilot_id = st.query_params.get("pilot")

if not pilot_id:
    st.error("No pilot selected.")
    st.stop()

pilot = load_pilot_data(pilot_id)

# Render header
header.render()

st.markdown(
    f"""
    <img src="{pilot['image']}" 
    style="width: 100%; max-height: 20vh; object-fit: cover; border-radius: 10px;">
    <h2>{pilot['city']} — {pilot['title']}</h2>
    """,
    unsafe_allow_html=True
)

# Tabs
tab_names = ["Pilot Info", "KPIs", "Dashboard"]
tab1, tab2, tab3 = st.tabs(tab_names)

with tab1:
    tab_info.render(pilot["tabs"]["Pilot Info"])

with tab2:
    tab_kpis.render(pilot["tabs"]["KPIs"])

with tab3:
    tab_dashboard.render(pilot["tabs"]["Dashboard"])

#Change tab based on query param
query = st.query_params
if "tab" in query:
    tab_name = query["tab"]
    if tab_name in tab_names:
        index_tab = tab_names.index(tab_name)

        # Simulate tab click via JS after page load
        js_code = f"""
        <script>
            window.addEventListener('load', function () {{
                const tab = window.parent.document.querySelectorAll('[data-baseweb="tab"]')[{index_tab}];
                if (tab) tab.click();
            }});
        </script>
        """
        components.v1.html(js_code, height=0)
    
# Render footer
footer.render()
