library(dplyr)
library(tidyverse)
library(sf)
library(mapview)
library(leaflet)
library(leafem)
library(sp)
library(svgtools)
library(geojsonio)

tab=read.csv(file = "sermons_hors_Hippo.csv")

#projection of GPS coordinates on a world map
position=data.frame(tab$numéro,tab$longitude,tab$latitude)
map=as_tibble(position)
map=map%>% drop_na() 
locations=st_as_sf(map, coords = c('tab.longitude', 'tab.latitude'), crs = 4326)
locations=st_jitter(locations,factor = 0.001) #pour éviter la superposition des points, ce qui rendrait la carte illisible

x=mapview(locations) %>%
  addStaticLabels(label = locations$tab.numéro,
                  noHide = TRUE,
                  direction = 'top',
                  textOnly = TRUE,
                  textsize = "20px")
 
  
x #view and export in html

#display distance in kms between Milev and Carthago
lonLat=as.matrix(data.frame(tab$longitude,tab$latitude)%>% drop_na() )
milev=as.matrix(t(data.frame(lonLat[21,])))
carthage=as.matrix(t(data.frame(lonLat[22,])))
thubuna=as.matrix(t(data.frame(lonLat[77,])))

hippone_df=data.frame(7.751272,36.882478)
colnames(hippone_df)=c("lon","lat")
hippone=as.matrix(hippone_df)

spDistsN1(hippone, carthage, longlat=TRUE)

mapshot(x, file = paste0(getwd(),"/file.png")) #save as png
