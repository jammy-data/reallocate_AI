import streamlit as st

def render():

    # st.image(
    #     pilot["image"],
    #     use_container_width=True,
    # )
    # st.markdown(f"## {pilot['city']} — {pilot['title']}")



    pages = {
        "Homepage": "pages/1_home.py",
        "Barcelona": "pages/Barcelona.py",
        "Gothenburg": "pages/Gothenburg.py",
        "Barcelona Kepler": "pages/Barcelona Kepler.py",
        "Barcelona Plotly": "pages/Barcelona Plotly.py",
    }

    cols = st.columns(len(pages))

    for col, (page_name, page_path) in zip(cols, pages.items()):
        with col:
            st.page_link(page=page_path, label=page_name)