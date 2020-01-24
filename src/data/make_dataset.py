""" Merge the data

...from the waypoints, survey sheets and photos """
import csv
import re
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


def main():
    """ Transform all the survey files
    
    Create a set of records for each waypoint with the date and species identified.
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
                # Add the date
                record = {'date': date_from_file(survey_file_path).isoformat()}
                for row in survey_file_reader:
                    # Get the waypoint information.
                    while 'species' not in row[0]:
                        record[row[0]] = row[1]
                        row = next(survey_file_reader)
                    # Get the individual species
                    while True:
                        record['species'] = row[1]
                        # write a species record
                        record_writer.writerow(record)
                        try:
                            row = next(survey_file_reader)
                        except StopIteration:
                            break # at the end of the file
                        if re.match(r'species|^$', row[0]) == None:
                            record[row[0]] = row[1] # add the read row to the record
                            break # at the end of the species list


if __name__ == "__main__":
    main()
