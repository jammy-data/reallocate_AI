import streamlit as st

create_page = st.Page("pages/1_home.py", title="Home", icon=":material/add_circle:")
delete_page = st.Page("pages/2_pilot.py", title="pilot", icon=":material/delete:")
test_page = st.Page("pages/Barcelona.py", title="Barcelona", icon=":material/delete:")


pg = st.navigation([create_page])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")

pg.run()
