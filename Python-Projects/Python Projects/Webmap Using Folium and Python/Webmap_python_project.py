import folium
import pandas as pd

data=pd.read_excel(r'iit_data.xlsx', encoder="unicode_escape")

iit_ranking=list(data["IIT Ranking"])
college_name=list(data["IIT College"])
Nirf_score=list(data["NIRF Score"])
lat=list(data["Latitude"])
lon=list(data["Longitude"])
pic=list(data["Image"])

#Parent Map
fg=folium.FeatureGroup("map")
fg.add_child(folium.GeoJson(data=(open("india_states.json","r",encoding="utf-8-sig").read())))
#utf means Unicode Transformation Format
# 8 is for 8 bit
# Sig means signature
# We use this because it treats file as BOM information instead of string



# HTML Code to use our dataset
for rank,name,score,lati,longi ,ima in zip(iit_ranking,college_name , Nirf_score , lat , lon , pic):
    fg.add_child(folium.Marker(Location=[lati,longi] , popup="<b>College Name : </b>"+ str(name)+
    "<br> <b>Rank among IIT in India :</b>" + str(rank)+
    "<br> <b>NIRF Score : </b>"+ str(score)+
    "<br> <b> img src "+ ima+
    "height=14,width=290>",icon=folium.Icon(color='red')))


map=folium.Map(Location=[20.0000,75.0000],zoom_start=4)
# Latitude and longitude when you open your file which location it will be visible
map.add_child(fg)
map.save("jh2.html")
