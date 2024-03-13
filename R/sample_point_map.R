library(leaflet.providers)
library(leaflet)
library(readr)
sample_points_path <- paste0("data/raw/spains-hall-waypoints-regular-30m",
                             "-with-name-edited.csv")
sample_points <- read_csv(sample_points_path)


# Create a leaflet map
m <- leaflet()

# Add map tiles
m <- addProviderTiles(m, "OpenStreetMap.Mapnik")

# Add markers for each point
for (i in 1:nrow(sample_points)) {
  m <- addMarkers(m, lng = sample_points$lon[i], lat = sample_points$lat[i])
}

# Display the map
m

