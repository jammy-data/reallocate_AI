import streamlit as st
from utils.data_loader import load_all_pilots
from datetime import datetime
# from utils.helpers import slugify  # We'll create this next

st.set_page_config(page_title="Pilot Overview", layout="wide")
st.title("🧭 Pilot Projects Overview")

pilots = load_all_pilots()

for pilot in pilots:
    name = pilot["name"]
    city = pilot["city"]
    title = pilot["title"]
    description = pilot.get("description", "No description available.")
    image_url = pilot.get("image", "")
    start = datetime.strptime(pilot["start_date"], "%Y-%m-%d").date()
    end = datetime.strptime(pilot["end_date"], "%Y-%m-%d").date()

    with st.expander(f"📍 {name}"):
        st.write(f"**City:** {city}")
        st.write(f"**Pilot Title:** {title}")
        st.write(f"**📅 Start:** {start}  📅 End:** {end}")
        st.write(f"📝 **Description:** {description}")
        st.image(image_url, caption=name, use_column_width="always")

        # Navigate to detailed page
        link = f"/1_Pilot?pilot={pilot['id']}"
        st.markdown(
            f"""<a href="{link}" target="_self">
                <button style="margin-top: 1rem;">Show more</button>
               </a>""",
            unsafe_allow_html=True,
        )
