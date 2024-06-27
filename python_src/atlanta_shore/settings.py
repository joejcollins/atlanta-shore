"""Global settings for the project."""

import datetime
import inspect
import os
from typing import Any

from atlanta_shore.file_finder_service import FileFinderService
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

    @property
    def observations_files(self) -> Any:
        """Get the list of file names."""
        file_finder = FileFinderService()
        data_files = file_finder.find_data_files(pattern="data-plant*.csv")
        return data_files


ATLANTA_SHORE = AtlantaShoreSettings()
