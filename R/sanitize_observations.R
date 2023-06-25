# Sanitize the observations dataset

library(readr)
sample_points_path <- paste0("data/raw/spains-hall-waypoints-regular-30m",
                             "-with-name-edited.csv")
sample_points <- read_csv(sample_points_path)

# Plotting Ordnance Survey Grid References
plot(sample_points$eastings, sample_points$northings,
     type = "p",
     pch = 16,
     col = "blue",
     xlab = "Eastings",
     ylab = "Northings",
     main = "Sample Points OS Grid")

eastings_origin <- min(sample_points$eastings) + 30
northings_origin <- min(sample_points$northings) + 30

# The points have a 30 metre separation so they and be standardized
sample_points$x <- (sample_points$eastings - eastings_origin) / 30
sample_points$y <- (sample_points$northings - northings_origin) / 30

# Plotting Ordnance the Standardized Grid
plot(sample_points$x, sample_points$y,
     type = "p",
     pch = 16,
     col = "red",
     xlab = "Eastings",
     ylab = "Northings",
     main = "Sample Points Standardized")

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
