# Sanitize the observations dataset


library(readr)
sample_points_path <- paste0("data/raw/spains-hall-waypoints-regular-30m",
                             "-with-name-edited.csv")
sample_points <- read_csv(sample_points_path)
# force the id to be an integer, not sure why this is necessary
sample_points$sample_point_id <- as.integer(sample_points$sample_point_id)

# Plotting Ordnance Survey Grid References
plot(sample_points$eastings, sample_points$northings,
     type = "p",
     pch = 16,
     col = "blue",
     xlab = "Eastings",
     ylab = "Northings",
     main = "Sample Points OS Grid")

eastings_origin <- min(sample_points$eastings)
northings_origin <- min(sample_points$northings)

# The points have a 30 metre separation so they and be standardized
sample_points$x <- ((sample_points$eastings - eastings_origin) / 30) + 1
sample_points$y <- ((sample_points$northings - northings_origin) / 30) + 1

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

# Check that all the points have the same number of observations
table(observations$sample_point_id)
length(unique(observations$sample_point_id))

# Make sure that the same ids are in both sets
sample_point_ids <- unlist(sample_points$sample_point_id)
observations_sample_point_ids <- unlist(unique(observations$sample_point_id))
setdiff(sample_point_ids, observations_sample_point_ids)
setdiff(observations_sample_point_ids,sample_point_ids)

library(dplyr)
observations_sample_point_11 <- observations %>% filter(sample_point_id == 11)
observations_sample_point_16 <- observations %>% filter(sample_point_id == 16)


# Outer join to get all the points
merged_data <- merge(observations, sample_points, by = "sample_point_id", all = TRUE)

# Wetness Estimates
library(ggplot2)

start_date <- as.Date("2019-01-01")
end_date <- as.Date("2019-12-31")

observations_year <- merged_data %>% filter(observation_date >= start_date & observation_date <= end_date)

ggplot(observations_year, aes(x, y, fill = wetness_estimate)) +
  geom_tile() +
  scale_fill_gradient(low = "white", high = "blue") + 
  labs(title = "Wetness Estimate 2019") +
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank(),
        axis.title.y=element_blank(),
        axis.text.y=element_blank(),
        axis.ticks.y=element_blank())

start_date <- as.Date("2020-01-01")
end_date <- as.Date("2020-12-31")

observations_year <- merged_data %>% filter(observation_date >= start_date & observation_date <= end_date)

ggplot(observations_year, aes(x, y, fill = wetness_estimate)) +
  geom_tile() +
  scale_fill_gradient(low = "white", high = "blue") + 
  labs(title = "Wetness Estimate 2020") +
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank(),
        axis.title.y=element_blank(),
        axis.text.y=element_blank(),
        axis.ticks.y=element_blank())

start_date <- as.Date("2021-01-01")
end_date <- as.Date("2021-12-31")

observations_year <- merged_data %>% filter(observation_date >= start_date & observation_date <= end_date)

ggplot(observations_year, aes(x, y, fill = wetness_estimate)) +
  geom_tile() +
  scale_fill_gradient(low = "white", high = "blue") + 
  labs(title = "Wetness Estimate 2021") +
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank(),
        axis.title.y=element_blank(),
        axis.text.y=element_blank(),
        axis.ticks.y=element_blank())

start_date <- as.Date("2022-01-01")
end_date <- as.Date("2022-12-31")

observations_year <- merged_data %>% filter(observation_date >= start_date & observation_date <= end_date)

ggplot(observations_year, aes(x, y, fill = wetness_estimate)) +
  geom_tile() +
  scale_fill_gradient(low = "white", high = "blue") + 
  labs(title = "Wetness Estimate 2022") +
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank(),
        axis.title.y=element_blank(),
        axis.text.y=element_blank(),
        axis.ticks.y=element_blank())

write.csv(merged_data, "data/processed/sample_point_observations.csv", row.names=FALSE)
