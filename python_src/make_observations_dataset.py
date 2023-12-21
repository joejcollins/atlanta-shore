""" Create the main observations data file by merging the observations files. """
import csv
from typing import List

from python_src.handlers.survey_file_reader import SurveyFileReader
from python_src.logger import setup_logger
from python_src.models.sample_point_observation import SamplePointObservation
from python_src.settings import ATLANTA_SHORE, date_from_file

LOG = setup_logger(__name__)


def _get_field_names(first_observations_file) -> List[str]:
    """Get the field names from the first observations file."""
    survey_file_reader = SurveyFileReader(first_observations_file)
    first_record = next(survey_file_reader)
    sample_point_observation = SamplePointObservation.set_values_from_observation_csv(
        first_record
    )
    return sample_point_observation.headers()


def create_observations_table() -> None:
    """Create the observations table"""
    # Get the headers from the first file.
    first_observations_file = ATLANTA_SHORE.observations_files[0]
    fieldnames = _get_field_names(first_observations_file)

    with open("./data/processed/observations.csv", "w+", newline="") as records_file:
        record_writer = csv.DictWriter(
            records_file,
            fieldnames=fieldnames,
        )
        record_writer.writeheader()
        for observations_file in ATLANTA_SHORE.observations_files:
            LOG.info(f"observations_file: {observations_file}")
            observation_date = date_from_file(observations_file)
            survey_file_reader = SurveyFileReader(observations_file)
            for record in survey_file_reader:
                LOG.debug(f"record: {record}")
                sample_point_observation = (
                    SamplePointObservation.set_values_from_observation_csv(record)
                )
                sample_point_observation.observation_date = observation_date
                record_writer.writerow(sample_point_observation.dict())


if __name__ == "__main__":
    create_observations_table()
    print("Done")
