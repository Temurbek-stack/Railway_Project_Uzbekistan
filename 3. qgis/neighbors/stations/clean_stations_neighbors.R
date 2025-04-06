# adjust the path here
#setwd("D:/github/UZRailways") #JASUR
setwd("E:/Github_repositories/UZRailways") #TEMURBEK

kaz <- st_read("2. geofabrik data/neighboring countries/kazakhstan_transport_infrastructure_shp/gis_osm_transport_free_1.shp")
afg <- st_read("2. geofabrik data/neighboring countries/afghanistan_transport_infrastructure_shp/gis_osm_transport_free_1.shp")
tkm <- st_read("2. geofabrik data/neighboring countries/turkmenistan_transport_infrastructure_shp/gis_osm_transport_free_1.shp")
taj <- st_read("2. geofabrik data/neighboring countries/tajikistan_transport_infrastructure_shp/gis_osm_transport_free_1.shp")
kgz <- st_read("2. geofabrik data/neighboring countries/kyrgyzstan_transport_infrastructure_shp/gis_osm_transport_free_1.shp")

kaz <- kaz %>%
  mutate(country = "kazakhstan")

afg <- afg %>%
  mutate(country = "afghanistan")

tkm <- tkm %>%
  mutate(country = "turkmenistan")

taj <- taj %>%
  mutate(country = "tajikistan")

kgz <- kgz %>%
  mutate(country = "kyrgyzstan")


stations_neigboring_countries <- rbind(kaz, afg, tkm, taj, kgz)

stations_neigboring_countries <- stations_neigboring_countries %>%
  filter(code == 5601 | code == 5602)

stations_neigboring_countries <- st_as_sf(stations_neigboring_countries)

st_write(stations_neigboring_countries, "3. qgis project/neighbors/stations/stations_neigboring_countries_shp.gpkg")

leaflet() %>%
  addTiles() %>%
  setView(lng = 64.5853, lat = 41, zoom = 6) %>%
  addCircleMarkers(data = stations_neigboring_countries, color = "black", radius = 1,
                   fill = TRUE, 
                   fillOpacity = 1, 
                   label = ~name, 
                   labelOptions = labelOptions(direction = "auto"))
