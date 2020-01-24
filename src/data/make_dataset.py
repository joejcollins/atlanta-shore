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


def get_next_quadrat(survey_file_reader):
    """ Find the quadrat details up to the first species """
    current_line = ['']
    quadrat_dict = {}
    while 'species' not in current_line[0]:
        current_line = next(survey_file_reader)
        quadrat_dict[current_line[0]] = current_line[1]
    return quadrat_dict


def get_the_rest_of_the_species(survey_file_reader):
    current_line = ['']
    while current_line[0] == '':
        current_line = next(survey_file_reader)
    return ""


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
                # Add the date, quadrat information and species to each record
                record = {'date': date_from_file(survey_file_path).isoformat()}
                quadrat = get_next_quadrat(survey_file_reader)
                record.update(quadrat)
                # TODO deal with remaining species at that waypoint
                record_writer.writerow(record)


if __name__ == "__main__":
    main()
