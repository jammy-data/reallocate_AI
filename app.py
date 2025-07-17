import streamlit as st
from streamlit import Page

# All your regular pages
home = Page("pages/1_home.py", title="Home", icon="🏠")
homepage = Page("Home.py", title="Old home page", icon="🏠")  # Assuming this is a separate home page
barcelona= Page("pages/Barcelona.py", title="Barcelona", icon="📄")
barcelona_kepler = Page("pages/Barcelona Kepler.py", title="Kepler Map", icon="🗺️")
barcelona_plotly = Page("pages/Barcelona Plotly.py", title="Plotly Map", icon="📊")
gothenburg = Page("pages/Gothenburg.py", title="Gothenburg", icon="📝")
pilot = Page("pages/2_pilot.py", title="Pilot", icon="🚫")
pilot = Page("pages/2_pilot.py", title="Pilot", icon="🚫")

# Include *all* pages in routing system so Streamlit can serve them
pg = st.navigation(
{
    "Home": [home,homepage],
    "Barcelona 🌆": [barcelona, barcelona_kepler, barcelona_plotly],
    "Gothenburg 🏙️": [gothenburg],
    "Pilot": [pilot]  # Pilot page is included here for routing
},
position="hidden"#Change to make pages visiable
)

pg.run()
