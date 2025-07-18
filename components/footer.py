import streamlit as st
from utils.layout import  show_logos_from_list
from utils.data_loader import load_logos
def render():
    logos = load_logos()
    st.write("### Footer")
    st.write("This is the footer section of the page.")
    st.write(logos)
    st.write("---")
    show_logos_from_list()  # Uses default LOGOS from layout    
    st.write("---")
