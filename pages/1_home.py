import streamlit as st
from utils.data_loader import load_generic_data
from datetime import datetime
# from utils.helpers import slugify  # We'll create this next

# st.set_page_config(page_title="Pilot Overview", layout="wide")
st.title("🧭 Pilot Projects Overview")

pages = [
    "pages/Barcelona.py",
    "pages/Gothenburg.py",
    "pages/Barcelona Kepler.py",
    "pages/Barcelona Plotly.py",
]

cols = st.columns(len(pages))

for col, page_path in zip(cols, pages):
    with col:
        st.page_link(page=page_path)

# Tab selector
tab = st.selectbox("Select a tab", ["Pilot Info", "KPIs", "Dashboard"])

# Load pilot data
pilots = load_generic_data() 

for pilot in pilots:
    name = pilot["name"]
    city = pilot["city"]
    title = pilot["title"]
    description = pilot.get("description", "No description available.")
    image_url = pilot.get("image", "")
    start = datetime.strptime(pilot["start_date"], "%d/%m/%Y").date()
    end = datetime.strptime(pilot["end_date"], "%d/%m/%Y").date()

    with st.expander(f"📍 {name}"):
        st.write(f"**City:** {city}")
        st.write(f"**Pilot Title:** {title}")
        st.write(f"**📅 Start:** {start}  **📅 End:** {end}")
        st.write(f"📝 **Description:** {description}")
        # st.image(image_url, caption=name, width=300)

        # Navigate to detailed page
        link = f"pilot?pilot={pilot['id']}&tab={tab}"
        st.markdown(
            f"""<a href="{link}" target="_self">
                <button style="margin-top: 1rem;">Show more</button>
               </a>""",
            unsafe_allow_html=True,
        )
