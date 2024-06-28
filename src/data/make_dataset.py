""" Merge the data

...from the waypoints, survey sheets and photos """
import csv
import datetime
import re

SURVEY_FILE_PATHS = [
    "./data/raw/2019-02/data-plant-2019-02-01-MEC.csv",
    "./data/raw/2019-02/data-plant-2019-02-02-MEC.csv",
    "./data/raw/2019-06/data-plant-2019-06-20-MEC.csv",
    "./data/raw/2019-06/data-plant-2019-06-21-MEC.csv",
    "./data/raw/2020-06/data-plant-2020-06-19-MEC.csv",
    "./data/raw/2020-06/data-plant-2020-06-20-MEC.csv",
    "./data/raw/2020-06/data-plant-2020-06-21-MEC.csv",
    "./data/raw/2021-06/data-plant-2021-06-20-MEC.csv",
    "./data/raw/2021-06/data-plant-2021-06-21-MEC.csv",
    "./data/raw/2022-06/data-plant-2022-06-24-MEC.csv",
    "./data/raw/2022-06/data-plant-2022-06-25-MEC.csv",
    "./data/raw/2022-06/data-plant-2022-06-26-MEC.csv",
    "./data/raw/2023-06/data-plant-2023-06-22-MEC.csv",
    "./data/raw/2023-06/data-plant-2023-06-23-MEC.csv",
    "./data/raw/2023-06/data-plant-2023-06-24-MEC.csv",
    "./data/raw/2023-06/data-plant-2023-06-25-MEC.csv",
]

SAMPLE_SITES_FILE_PATH = "./data/raw/spains-hall-waypoints-regular-30m-with-name.gpx"


def date_from_file(file_path):
    """Extract the survey date from the survey file path"""
    split_path = file_path.split("-")
    year = int(split_path[-4])
    month = int(split_path[-3])
    day = int(split_path[-2])
    return datetime.date(year, month, day)


def create_records_table():
    """Transform all the survey files into a records list

    Create a records for each waypoint with the date and species identified.
    """
    with open("./data/processed/records.csv", "w+", newline="") as records_file:
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

        for survey_file_path in SURVEY_FILE_PATHS:
            print(survey_file_path)
            with open(survey_file_path, newline="") as survey_file:
                survey_file_reader = csv.reader(survey_file, delimiter=",")
                # Prepare an empty record with the file date
                record = {
                    "date": date_from_file(survey_file_path).isoformat(),
                    "comments": "",
                }
                waypoint_comments = ""  # to collect waypoint comments
                for row in survey_file_reader:
                    # Read the waypoint information into the record.
                    while "species" not in row[0]:
                        record[row[0]] = row[1]  # so just add it to the record
                        if row[2]:  # there is a comment
                            waypoint_comments = waypoint_comments + row[2]
                        row = next(survey_file_reader)
                    # Get the individual species records
                    while True:
                        record["comments"] = waypoint_comments
                        record["species"] = row[1]
                        if row[2]:  # there is a comment
                            record["comments"] = record["comments"] + " - " + row[2]
                        # write a species record
                        record_writer.writerow(record)
                        try:
                            row = next(survey_file_reader)
                        except StopIteration:
                            break  # at the end of the file
                        if re.match(r"species|^$", row[0]) is None:
                            # Next waypoint so add the read row to the record
                            record[row[0]] = row[1]
                            waypoint_comments = row[2] or ""
                            break  # at the end of the species list


if __name__ == "__main__":
    create_records_table()
