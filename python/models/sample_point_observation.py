"""Schema for an observation at a sampling point."""
import csv
from datetime import date
from io import StringIO
from typing import List, Optional

from pydantic import BaseModel,  Field


class SamplePointObservation(BaseModel):
    """The point observations are all recorded in the yellow field book.  And are
    entered into a csv file using the same layout as the field book.  The field booklets
    use a different naming convention to the data tables, because the field booklets
    were created in a hurry without due attention."""

    sample_point_id: int = Field(alias='quadrat')
    observation_date: date = Optional[date]
    garmin_waypoint_id: int = Field(alias="waypoint")  # Garmin Waypoints file.
    garmin_grid_ref: str = Field(alias="grid_reference")  # If the Garmin file fails.
    photo_up_id: str = Field(alias="photo_up")
    photo_down_id: str = Field(alias="photo_down")
    wetness_estimate: int = Field(alias="wetness")  # estimated wetness of the ground.
    canopy_cover_estimate: int = Field(alias="canopy")  # estimated percentage cover.
    species_identified: List[str] = Field(alias="species")  # list of species found.

    @classmethod
    def set_values_from_observation_csv(
        cls, observation_csv: str
    ) -> "SamplePointObservation":
        """Set the values of the model from the csv observation record."""
        csv_data = csv.reader(observation_csv.splitlines())
        data = {}
        for row in csv_data:
            csv_field_name = row[0]
            csv_field_value = row[1]
            # The species list is a special case, because it is a list of values.
            if csv_field_name in ['species', ""]:
                # Create a list for the species if it is not there then add.
                if 'species' not in data:
                    data['species'] = []
                data['species'].append(csv_field_value)
            else:
                data[csv_field_name] = csv_field_value

        return cls(**data)

    def as_csv(self) -> str:
        """Return the observation as csv."""
        field_names = list(self.__fields__.keys())
        data = [self.dict()]
        csv_string = ''

        with StringIO() as csv:
            writer = csv.DictWriter(csv, fieldnames=field_names)
            writer.writerows(data)
            csv_string = csv.getvalue()
        return csv_string
