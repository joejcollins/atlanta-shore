"""Global settings for the project."""

import datetime
import json
from pathlib import Path
from typing import Any

from atlanta_shore import file_finder_service


def date_from_file(file_path: str) -> datetime.date:
    """Extract the survey date from the survey file path"""
    split_path = file_path.split("-")
    year = int(split_path[-4])
    month = int(split_path[-3])
    day = int(split_path[-2])
    return datetime.date(year, month, day)


class AtlantaShoreSettings:
    """Settings for the Atlanta Shore Project."""

    def __init__(
        self, file_finder=file_finder_service.FileFinderService(), file_opener=open
    ):
        """Load the file finder, file opener and local settings."""
        self.file_finder = file_finder
        self.open = file_opener
        self.load_local_settings()

    # region Static settings which can be over ridden with the `settings.json` file.
    log_format: str = (
        "[%(asctime)s] [%(levelname)s] %(message)s. "
        "%(pathname)s:%(lineno)d, in %(funcName)s()"
    )
    log_level: str = "WARN"  # as a string so it can be read and set in settings.json.

    # endregion

    def load_local_settings(self) -> None:
        """Load custom settings from the local settings.json file."""
        if settings_path := self.file_finder.find_file_upwards("settings.json"):
            with self.open(settings_path, "r", encoding="utf-8") as file:
                content = file.read()
                settings = json.loads(content)
                for key, value in settings.items():
                    if hasattr(self, key):
                        setattr(self, key, value)

    # region Properties
    @property
    def observations_files(self) -> Any:
        """Get the list of file names."""
        return self.file_finder.find_data_files(pattern="data-plant*.csv")

    @property
    def processed_data(self) -> Any:
        """Get the directory for processed data."""
        root = self.file_finder.find_root()
        return Path(root) / "data/processed"

    # endregion


ATLANTA_SHORE = AtlantaShoreSettings()
