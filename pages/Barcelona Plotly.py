# app.py
import os
import sys
import streamlit as st
import geopandas as gpd
import plotly.express as px
from shapely.geometry import Point
from dotenv import load_dotenv

from utils.helpers import load_parquet_from_ckan  # Custom function
from utils.layout import  show_logos_from_list

# Ensure project root is in path for module discovery
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)



# -------------------------- CONFIG --------------------------
load_dotenv()

DATASETS = {
    "Walking journeys": "trips_walking",
    "Bike & PMV by sex": "bike_and_pmv_by_sex",
    "Public accessibility": "streets_accessibility"
}

# ---------------------- HELPER FUNCTIONS ----------------------

def display_geodata(df):
    if "geometry" not in df.columns:
        df = df.copy()
        df["geometry"] = gpd.points_from_xy(df["Gis_X"], df["Gis_Y"], crs="EPSG:25831")
    gdf = gpd.GeoDataFrame(df, geometry="geometry").to_crs("EPSG:4326")

    gdf["GIS_lat"] = gdf.geometry.y
    gdf["GIS_long"] = gdf.geometry.x

    geo_cols = [col for col in gdf.columns if 'GIS' in col.upper()]
    time_cols = [col for col in gdf.columns if 'Data' in col]
    exclude = geo_cols + time_cols + ["geometry"]
    VARIABLES = [col for col in gdf.columns if col not in exclude]

    variable_name = st.selectbox("Choose a variable", VARIABLES)

    fig = px.scatter_map(
        gdf,
        lat="GIS_lat",
        lon="GIS_long",
        color=variable_name,
        zoom=10,
        hover_data={
            "Data d'Alta": True,
            "Situació": True,
            "GIS_lat": False,
            "GIS_long": False
        }
    )
    fig.update_layout(map_style="carto-darkmatter")
    st.plotly_chart(fig)

def display_timeseries(df):
    time_col = 'Dim-00:TEMPS'
    VARIABLES = [col for col in df.columns if col != time_col]

    variable_name = st.selectbox("Choose a variable", VARIABLES)
    grouped = df.groupby([time_col, variable_name]).sum(numeric_only=True).reset_index()

    fig = px.line(
        grouped,
        x=time_col,
        y='VALUE',
        color=variable_name,
        title=f"Overview of {variable_name}"
    )
    st.plotly_chart(fig)

# ---------------------- MAIN APP ----------------------

def main():
    st.set_page_config(page_title="Dataset Explorer")
    st.logo("images/reallocate_logo.png", size='large')
    st.title("Dataset Explorer")

    if st.button("Homepage"):
        st.switch_page("Home.py")

    dataset_name = st.selectbox("Choose a dataset", list(DATASETS.keys()))
    dataset_key = DATASETS[dataset_name]

    try:
        df = load_parquet_from_ckan(dataset_key)
        st.write(f"Preview of **{dataset_name}**:")
        st.dataframe(df.head())

        if 'Gis_X' in df.columns and 'Gis_Y' in df.columns:
            display_geodata(df)
        else:
            display_timeseries(df)

    except Exception as e:
        st.error(f"Failed to load data: {e}")

    st.write("---")
    show_logos_from_list()  # Uses default LOGOS from layout    
    st.write("---")

if __name__ == "__main__":
    main()
