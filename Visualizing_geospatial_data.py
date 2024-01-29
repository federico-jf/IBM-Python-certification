#Python practice
#Federico Ferrero
#Visualizing Geosptial Data


import numpy as np
import pandas as pd

#!pip3 install folium==0.5.0
import folium

#define the world mao
world_map = folium.Map()

world_map

#create a map centered in Canada with a low zoom level
world_map = folium.Map(location=[56.130, -106.35], zoom_start = 4)

world_map

#add black and white feature
world_map = folium.Map(location=[56.130, -106.35], zoom_start = 4, tiles = 'Cartodb dark_matter')


#add minimalistic feature
world_map = folium.Map(location=[56.130, -106.35], zoom_start = 4, tiles = 'Cartodb positron')

#superimpose the locations of the crimes onto the map: feature group

incidents = folium.map.FeatureGroup()
for lat, lng, in zip(df_incidents.Y, df_incidents.X):
  incidents.add_child(
    folium.vector_layers.CircleMarker(
      [lat, lng],
      radius=5,
      color='yellow',
      fill=True,
      fill_color='blue',
      fill_opacity=0.6
    )
  )
sanfran_map.add_child(incidents)

#let's add a category of the crime

#cluster the type of crimes


######### CHOROPLET MAPS
######### IT NEEDS ALSO A GeoJSON file that defines the areas/boundaries of the state, county, or country we are interested in.
#########



