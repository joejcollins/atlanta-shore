"""Schema for a sampling point."""
from pydantic import BaseModel


class SamplePoint(BaseModel):
    """The sample points were laid out on a 30 metre grid.

    Following the British National Grid. The eastings and northings are the coordinates
    on the grid."""
    id: int
    description: str
    eastings: int
    northings: int
    latitude: float
    longitude: float
    os_grid_ref: str
