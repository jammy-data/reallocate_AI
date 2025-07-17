# utils/layout.py

import streamlit as st

LOGOS = [
    {
        "src": "https://reallocatemobility.eu/maintemplate/data/logos/logo.png",
        "href": "https://reallocatemobility.eu",
        "alt": "Reallocate Logo"
    },
    {
        "src": "https://www.bsc.es/sites/default/files/public/styles/bscw2_-_simple_crop_style/public/bscw2/pages/discover-bsc/bsc-branding-identity-logo-header_0.jpg?itok=BdjkMwL6&sc=569a3a63c536723072a6d292da3890ca",
        "href": "https://www.bsc.es",
        "alt": "BSC Logo"
    }
]

def show_logo_image():
    st.image("assets/images/reallocate_logo.png", width=200)

def show_separator():
    st.markdown("---")

def show_logos_from_list(logos=LOGOS):  # Default to the global LOGOS
    css = """
    <style>
    .image-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 20px;
        margin: 20px 0;
    }
    .image-container img {
        max-height: 80px;
        max-width: 150px;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

    html = '<div class="image-container">'
    for logo in logos:
        html += f'<a href="{logo["href"]}" target="_blank"><img src="{logo["src"]}" alt="{logo["alt"]}"></a>'
    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)
