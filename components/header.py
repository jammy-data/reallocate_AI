import streamlit as st

def render(pilot):
    st.image(pilot["image"], width=300)
    st.markdown(f"## {pilot['city']} — {pilot['title']}")
