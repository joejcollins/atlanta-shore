library(readr)
sample_points <- read_csv("data/raw/spains-hall-waypoints-regular-30m-with-name-edited.csv")

eastings_origin <- min(sample_points$eastings)
northings_origin <- min(sample_points$northings)

# The points have a 30 metre separation
sample_points$x <- (sample_points$eastings - eastings_origin) / 30
sample_points$y <- (sample_points$northings - northings_origin) / 30


                    