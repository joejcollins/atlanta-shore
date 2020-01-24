""" Merge the data

...from the waypoints, survey sheets and photos """
import csv
import datetime

SURVEY_FILE_PATHS = ["./data/raw/2019-02/data-plant-2019-02-01-MEC.csv",
                     "./data/raw/2019-02/data-plant-2019-02-02-MEC.csv",
                     "./data/raw/2019-06/data-plant-2019-06-20-MEC.csv",
                     "./data/raw/2019-06/data-plant-2019-06-21-MEC.csv"]

def date_from_file(file_path):
    """ Extract the survey date from the survey file path """
    split_path = file_path.split("-")
    year = int(split_path[-4])
    month = int(split_path[-3])
    day = int(split_path[-2])
    return datetime.date(year, month, day)


def get_next_quadrat(csv_reader):
    """ Find the quadrat details up to the first 'species' """
    quadrat = "dummy"
    waypoint = "dummy"
    grid_reference = "dummy"
    photo_up = "dummy"
    photo_down = "dummy"
    wetness = "dummy"
    canopy = "dummy"
    species = "dummy"
    return {
        'quadrat': quadrat,
        'waypoint': waypoint,
        'grid_reference': grid_reference,
        'photo_up': photo_up,
        'photo_down': photo_down,
        'wetness': wetness,
        'canopy': canopy,
        'species': species
        }


def main():
    """ Transform all the  survey files 
    
    Create a set of records for each quadrat with the date and species identified.
    """
    with open("./data/processed/records.csv", 'w+', newline='') as records_file:
        record_writer = csv.DictWriter(records_file, fieldnames=["date", "quadrat", "waypoint",
                                                                 "grid_reference", "photo_up",
                                                                 "photo_down", "wetness",
                                                                 "canopy", "species"])
        record_writer.writeheader()

        for survey_file_path in SURVEY_FILE_PATHS:
            with open(survey_file_path, newline='') as survey_file:
                survey_file_reader = csv.reader(survey_file, delimiter=',')
                quadrat = get_next_quadrat(survey_file_reader)
                for row in survey_file_reader:
                    # add the date, quadrat information and species to each record
                    record = {'date': date_from_file(survey_file_path).isoformat()}
                    quadrat = get_next_quadrat(survey_file_reader)
                    record.update(quadrat)
                    species = {'species': "Dummius speciesus maximus"}
                    record.update(species)
                    record_writer.writerow(record)


if __name__ == "__main__":
    main()
