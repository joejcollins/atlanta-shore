library(readr)
sample_points <- read_csv("data/raw/spains-hall-waypoints-regular-30m-with-name-edited.csv")

eastings_origin <- min(sample_points$eastings)
northings_origin <- min(sample_points$northings)

# The points have a 30 metre separation
sample_points$x <- (sample_points$eastings - eastings_origin + 15) / 30
sample_points$y <- (sample_points$northings - northings_origin + 15) / 30

observations <- read.csv("data/processed/observations.csv")
observations$observation_date <- as.Date(observations$observation_date)

merged_data <- merge(observations, sample_points, by = "sample_point_id")

library(dplyr)
start_date <- as.Date("2021-01-01")
end_date <- as.Date("2021-12-31")

observations_year <- merged_data %>% filter(observation_date >= start_date & observation_date <= end_date)

library(ggplot2)
ggplot(observations_year, aes(x, y, fill = wetness_estimate)) +
  geom_tile() +
  scale_fill_gradient(low = "white", high = "blue")

