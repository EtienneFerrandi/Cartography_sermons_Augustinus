#!/usr/bin/python

import requests
import pandas as pd

carthage="https://pleiades.stoa.org/places/314921/json" #pid de Carthage
hippone="https://pleiades.stoa.org/places/305090/json" #pid d'Hippone
hippo_diarrhytus="https://pleiades.stoa.org/places/315038/json" #pid d'Hippo Diarrhytus
chusa="https://pleiades.stoa.org/places/619139/json" #pid de Chusa
milev="https://pleiades.stoa.org/places/305109/json" #pid de Milev
bulla_regia="https://pleiades.stoa.org/places/314912/json" #pid de Bulla Regia
utique="https://pleiades.stoa.org/places/315248/json" #pid d'Utique
thignica="https://pleiades.stoa.org/places/315207/json" #pid de Thignica
boseth="https://pleiades.stoa.org/places/321647/json" #pid de Boseth
thubuna="https://pleiades.stoa.org/places/334641/json" #pid de Tuneba

liste_lieux=[carthage, hippone, hippo_diarrhytus, chusa, milev, bulla_regia, utique, thignica, thubuna] 
#boseth non géolocalisée
#chusa géolocalisée en Asie mineure...

longitudes=[]
latitudes=[]
for i in liste_lieux:
    response=requests.get(i).json()
    coordinates=response['features'][0]['geometry']['coordinates']
    longitudes.append(coordinates[0])
    latitudes.append(coordinates[1])  
    
df=pd.read_csv("sermons_hors_Hippone.csv")
df["longitude"]=""
df["latitude"]=""

df.loc[df["lieu"] == 'Carthage', 'longitude'] = longitudes[0]
df.loc[df["lieu"] == 'Carthage', 'latitude'] = latitudes[0]

df.loc[df["lieu"] == 'Hippone', 'longitude'] = longitudes[1]
df.loc[df["lieu"] == 'Hippone', 'latitude'] = latitudes[1]

df.loc[df["lieu"] == 'Hippo Diarrhytus', 'longitude'] = longitudes[2]
df.loc[df["lieu"] == 'Hippo Diarrhytus', 'latitude'] = latitudes[2]

df.loc[df["lieu"] == 'Milev', 'longitude'] = longitudes[4]
df.loc[df["lieu"] == 'Milev', 'latitude'] = latitudes[4]

df.loc[df["lieu"] == 'Bulla Regia', 'longitude'] = longitudes[5]
df.loc[df["lieu"] == 'Bulla Regia', 'latitude'] = latitudes[5]

df.loc[df["lieu"] == 'Utique', 'longitude'] = longitudes[6]
df.loc[df["lieu"] == 'Utique', 'latitude'] = latitudes[6]

df.loc[df["lieu"] == 'Thignica', 'longitude'] = longitudes[7]
df.loc[df["lieu"] == 'Thignica', 'latitude'] = latitudes[7]

df.loc[df["lieu"] == 'Thubuna', 'longitude'] = longitudes[8]
df.loc[df["lieu"] == 'Thubuna', 'latitude'] = latitudes[8]

df.to_csv("sermons_hors_Hippo.csv")
