import streamlit as st

def render(info):
    st.markdown(f"### Description")
    st.write(info.get("description", "No description available."))

    st.markdown(f"### Location")
    st.write(info.get("location_description", "No location description provided."))

    # Optional: map placeholder
    st.map({
        "lat": [info["location"]["lat"]],
        "lon": [info["location"]["lon"]]
    }) if "location" in info else st.write("Map data not available.")
