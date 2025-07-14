import streamlit as st

def show_logos():
    st.markdown(
        """
        <style>
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
            margin-top: 20px;
            margin-bottom: 20px;
        }

        .image-container img {
            height: auto;
            max-height: 80px;
            width: auto;
            max-width: 150px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="image-container">
            <a href="https://reallocatemobility.eu" target="_blank">
                <img src="https://reallocatemobility.eu/maintemplate/data/logos/logo.png" alt="Reallocate Logo">
            </a>
            <a href="https://www.bsc.es" target="_blank">
                <img src="https://www.bsc.es/sites/default/files/public/styles/bscw2_-_simple_crop_style/public/bscw2/pages/discover-bsc/bsc-branding-identity-logo-header_0.jpg?itok=BdjkMwL6&sc=569a3a63c536723072a6d292da3890ca" alt="Partner Logo">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

def show_separator():
    st.write("---")

def show_logo_image():
    st.logo("images/reallocate_logo.png", size="large")
