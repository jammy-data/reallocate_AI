import streamlit as st

def render(pilot):

    # st.image(
    #     pilot["image"],
    #     use_container_width=True,
    # )
    # st.markdown(f"## {pilot['city']} — {pilot['title']}")

    st.markdown(
        f"""
        <img src="{pilot['image']}" 
             style="width: 100%; max-height: 40vh; object-fit: cover; border-radius: 10px;">
        <h2>{pilot['city']} — {pilot['title']}</h2>
        """,
        unsafe_allow_html=True
    )
