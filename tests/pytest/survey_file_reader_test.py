"""Confirm that the survey file reader can iterate through a file."""
from python.handlers.survey_file_reader import SurveyFileReader


def test_read_first_record() -> None:
    """Confirm that the first record can be read."""
    # Arrange
    survey_file_reader = SurveyFileReader("tests/pytest/dummy_survey_file.csv")
    # Act
    record = next(survey_file_reader)
    # Assert
    assert record.startswith("quadrat,63,\nwaypoint,1,\ngrid_reference,TL6769933268,")


def test_read_last_record() -> None:
    """Confirm that the last record can be read."""
    # Arrange
    survey_file_reader = SurveyFileReader("tests/pytest/dummy_survey_file.csv")
    # Act
    record = None
    for record in survey_file_reader:
        pass
    # Assert
    assert record.endswith(",,,")
