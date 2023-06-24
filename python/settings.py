"""Global settings for the project."""
import inspect
import os
from dataclasses import dataclass


def this_directory() -> str:
    """Inspect the stack to find out where I have been called from."""
    # This approach is used to avoid relying on the location of the file.
    # The calling frame is the second frame in the stack.
    calling_frame = inspect.stack()[1]
    calling_file_path = calling_frame.filename
    return os.path.dirname(calling_file_path)


@dataclass
class AtlantaShoreSettings:
    """Settings for the Atlanta Shore Project."""

    log_format: str = "[%(asctime)s] [%(levelname)s] %(message)s. %(pathname)s:%(lineno)d, in %(funcName)s()"
    log_level: str = "WARN"  # as a string so it can be read and set in a settings.json.

    observations_files = [
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
