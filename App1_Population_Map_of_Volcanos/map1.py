import folium #import folium for map based geocoding
import pandas #import pandas for reading csv file


#function to differentiate popups by risk
def color_producer(risk_level):
    if risk_level == 3:
        return "red"
    elif risk_level == 2:
        return "orange"
    elif risk_level == 1:
        return "green"
    else:
        return "lightgray"


#Read csv file
data = pandas.read_csv("App1_Population_Map_of_Volcanos/volcano.csv")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
name = list(data["V_Name"])
rsk = list(data["risk"])

#Define a Location to display while opening
map = folium.Map(location=[13.075748,80.181646], zoom_start=10, tiles="Stamen Terrain")

#Define a Feature Group
fgv = folium.FeatureGroup(name="Volcanos")
#Define Features in the Feature Group
for lt, ln, nme, rk in zip(lat, lon, name, rsk):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=nme, fill_color=color_producer(rk), color='grey', fill=True, fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("App1_Population_Map_of_Volcanos/world.json", 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
#Save as html file
map.save("App1_Population_Map_of_Volcanos/Map1.html")