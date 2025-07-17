import streamlit as st

from st_pages import add_page_title, get_nav_from_toml, hide_pages

st.set_page_config(layout="wide")

# hide_pages(["Pilot"])

sections = st.sidebar.toggle("Sections", value=True, key="use_sections")

nav = get_nav_from_toml(
    ".streamlit/pages_sections.toml" if sections else ".streamlit/pages.toml"
)


pg = st.navigation(nav)

add_page_title(pg)

pg.run()