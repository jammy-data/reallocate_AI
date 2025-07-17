# app.py
import os
import sys
import streamlit as st
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import geopandas as gpd
import plotly.express as px
from shapely.geometry import Point
from dotenv import load_dotenv

from utils.helpers import load_parquet_from_ckan  # Custom function
from utils.layout import  show_logos_from_list
from utils.constants import DATASETS
# Ensure project root is in path for module discovery
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)



# -------------------------- CONFIG --------------------------
load_dotenv()

# ---------------------- HELPER FUNCTIONS ----------------------

def display_geodata(df):
    if "geometry" not in df.columns:
        df = df.copy()
        df["geometry"] = gpd.points_from_xy(df["Gis_X"], df["Gis_Y"], crs="EPSG:25831")
    gdf = gpd.GeoDataFrame(df, geometry="geometry").to_crs("EPSG:4326")

    # KeplerGl expects lat/lon columns
    gdf["lat"] = gdf.geometry.y
    gdf["lon"] = gdf.geometry.x

    # Select columns to show in KeplerGl
    show_cols = [col for col in gdf.columns if col not in ["geometry"]]
    geo_cols = [col for col in gdf.columns if 'GIS' in col.upper()]
    time_cols = [col for col in gdf.columns if 'Data' in col]
    exclude = geo_cols + time_cols + ["geometry"]
    VARIABLES = [col for col in gdf.columns if col not in exclude]

    variable_name = st.selectbox("Choose a variable", VARIABLES)
    # Prepare data for KeplerGl
    kepler_data = gdf[show_cols]

    config = {
        "version": "v1",
        "config": {
            "visState": {
                "filters": [],
                "layers": [
                    {
                        "id": "layer_1",
                        "type": "point",
                        "config": {
                            "dataId": "Geodata",
                            "label": variable_name,
                            "color": [255, 0, 0],
                            "columns": {
                                "lat": "lat",
                                "lng": "lon",
                                "altitude": None
                            },
                            "isVisible": True,
                            "visConfig": {
                                "radius": 1,
                                "fixedRadius": False,
                                "opacity": 0.8,
                                "outline": False
                            }
                        }
                    }
                ],
                "interactionConfig": {
                    "tooltip": {
                        "fieldsToShow": {
                            variable_name: ["VALUE"]
                        },
                        "enabled": True
                    }
                }
            }

        },        
    }
    map_ = KeplerGl(height=600)
    map_.add_data(data=kepler_data, name="Geodata")
    map_.config = config
    keplergl_static(map_,height=600,center_map=True,read_only=True)

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
    # st.set_page_config(page_title="Dataset Explorer")
    st.logo("assets/images/reallocate_logo.png", size='large')
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
