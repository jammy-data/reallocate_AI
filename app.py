import streamlit as st
from streamlit import Page

st.set_page_config(layout="wide")

# All your regular pages
home = Page("pages/1_home.py", title="Home", icon="🏠")
barcelona= Page("pages/old/Barcelona.py", title="Barcelona", icon="📄")
barcelona_kepler = Page("pages/old/Barcelona Kepler.py", title="Kepler Map", icon="🗺️")
barcelona_plotly = Page("pages/old/Barcelona Plotly.py", title="Plotly Map", icon="📊")
gothenburg = Page("pages/old/Gothenburg.py", title="Gothenburg", icon="📝")
pilot = Page("pages/2_pilot.py", title="Pilot", icon="👨‍✈️")

# Include *all* pages in routing system so Streamlit can serve them
pg = st.navigation(
{
    "Home": [home],
    "Barcelona 🌆": [barcelona, barcelona_kepler, barcelona_plotly],
    "Gothenburg 🏙️": [gothenburg],
    "Pilot": [pilot]  # Pilot page is included here for routing
},
position="hidden"#Change to make pages visiable
)

pg.run()
