""" Merge the data

...from the waypoints, survey sheets and photos """
import csv

FILES = ["/data/raw/2019-02/data-plant-2019-02-01-MEC.csv",
         "/data/raw/2019-02/data-plant-2019-02-02-MEC.csv",
         "/data/raw/2019-06/data-plant-2019-06-20-MEC.csv",
         "/data/raw/2019-06/data-plant-2019-06-21-MEC.csv"]


def main():
    """ Transform all the files """
    with open("./data/processed/records.csv", 'w', newline='') as records_file:
        record_writer = csv.writer(records_file, delimiter=' ',
                                   quotechar='|', quoting=csv.QUOTE_MINIMAL)
        record_writer.writerow("test") 
    for survey_file in FILES:
        pass


if __name__ == "__main__":
    main()
