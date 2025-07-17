import streamlit as st

def render(pilot):
    st.image(pilot["image"])
    st.markdown(f"## {pilot['city']} — {pilot['title']}")
