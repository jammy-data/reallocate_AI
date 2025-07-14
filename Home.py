import streamlit as st
from utils.layout import show_logos, show_separator, show_logo_image
from utils.constants import PILOTS

st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

show_logo_image()

st.title("Reallocate Pilots")

with st.form("pilot_form"):
    pilot_name = st.selectbox("Choose a pilot", PILOTS)
    submitted = st.form_submit_button("Go to pilot page")
    if submitted:
        st.switch_page(f"pages/{pilot_name}.py")

show_separator()
show_logos()
show_separator()
