"""Global settings for the project."""
import datetime
import inspect
import os
from typing import List

from pydantic import BaseModel


def this_directory() -> str:
    """Inspect the stack to find out where I have been called from."""
    # This approach is used to avoid relying on the location of the file.
    # The calling frame is the second frame in the stack.
    calling_frame = inspect.stack()[1]
    calling_file_path = calling_frame.filename
    return os.path.dirname(calling_file_path)


def date_from_file(file_path: str) -> datetime.date:
    """Extract the survey date from the survey file path"""
    split_path = file_path.split("-")
    year = int(split_path[-4])
    month = int(split_path[-3])
    day = int(split_path[-2])
    return datetime.date(year, month, day)


class AtlantaShoreSettings(BaseModel):
    """Settings for the Atlanta Shore Project."""

    log_format: str = (
        "[%(asctime)s] [%(levelname)s] %(message)s. "
        "%(pathname)s:%(lineno)d, in %(funcName)s()"
    )
    log_level: str = "WARN"  # as a string so it can be read and set in settings.json.

    data_files: List[str] = [
        "2019-02/data-plant-2019-02-01-MEC.csv",
        "2019-02/data-plant-2019-02-02-MEC.csv",
        "2019-06/data-plant-2019-06-20-MEC.csv",
        "2019-06/data-plant-2019-06-21-MEC.csv",
        "2020-06/data-plant-2020-06-19-MEC.csv",
        "2020-06/data-plant-2020-06-20-MEC.csv",
        "2020-06/data-plant-2020-06-21-MEC.csv",
        "2021-06/data-plant-2021-06-20-MEC.csv",
        "2021-06/data-plant-2021-06-21-MEC.csv",
        "2022-06/data-plant-2022-06-24-MEC.csv",
        "2022-06/data-plant-2022-06-25-MEC.csv",
        "2022-06/data-plant-2022-06-26-MEC.csv",
    ]

    @property
    def observations_files(self) -> List[str]:
        """Return the observation file paths as a list of strings."""
        data_directory = "./data/raw"
        return [f"{data_directory}/{data_file}" for data_file in self.data_files]


ATLANTA_SHORE = AtlantaShoreSettings()
