import streamlit as st

def render(info):
    st.markdown(f"### Description")
    st.write(info.get("description", "No description available."))

    st.markdown(f"### Location")
    st.write(info.get("location", "No location description provided."))

    # Optional: map placeholder
    if "lat" in info and "lon" in info:
        try:
            lat = float(str(info["lat"]).replace(",", "."))
            lon = float(str(info["lon"]).replace(",", "."))
            st.map({"lat": [lat], "lon": [lon]})
        except Exception:
            st.write("Invalid latitude or longitude format.")
    else:
        st.write("Map data not available.")
