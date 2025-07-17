import streamlit as st

def render(pilot):
    st.image(pilot["image"], use_column_width=True)
    st.markdown(f"## {pilot['city']} — {pilot['title']}")
