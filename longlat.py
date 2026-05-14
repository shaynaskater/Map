# Create a streamlit app where a user enters longitude and latitude and it creates a map with with a little icon over the spot that you selected. Submit a file longlat.py and loglat.gif of it working
#streamlit-folium

#streamlit 
# streamlit run "/Users/shaynademick/Downloads/Hw6/longlat.py"  
import streamlit as st
from streamlit_folium import st_folium
import folium

st.set_page_config(layout="wide")
st.markdown("# Map")
st.markdown("### Please input a latitude and longitude to see your map.")

col1, col2 = st.columns(2)
with col1:
    x = st.number_input("Latitude", value=None, placeholder="Enter Latitude", min_value=-90.0, max_value=90.0)
with col2:
    y = st.number_input("Longitude", value=None, placeholder="Enter Longitude", min_value=-180.0, max_value=180.0)

# Map is OUTSIDE the columns block — renders full width below
if x is not None and y is not None:
    m = folium.Map(location=[x, y], zoom_start=10)
    folium.Marker([x, y], popup="Location", tooltip="Location").add_to(m)
    st_data = st_folium(m, use_container_width=True) 
else:
    st.info("Enter a latitude and longitude above to display the map.")