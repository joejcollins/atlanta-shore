""" Merge the data

...from the waypoints, survey sheets and photos """
import csv
import datetime

from python_src.models.sample_point_observation import SamplePointObservation
from python_src.settings import AtlantaShoreSettings


def date_from_file(file_path):
    """Extract the survey date from the survey file path"""
    split_path = file_path.split("-")
    year = int(split_path[-4])
    month = int(split_path[-3])
    day = int(split_path[-2])
    return datetime.date(year, month, day)


def create_observations_table():
    """Create the observations table"""
    settings = AtlantaShoreSettings()
    first_observations_file = settings.observations_files[0]
    

    with open("./data/processed/observations.csv", "w+", newline="") as records_file:
        record_writer = csv.DictWriter(
            records_file,
            fieldnames=[
                "date",
                "quadrat",
                "waypoint",
                "grid_reference",
                "photo_up",
                "photo_down",
                "wetness",
                "canopy",
                "species",
                "comments",
            ],
        )
        record_writer.writeheader()


if __name__ == "__main__":
    create_observations_table()
