"""Schema for a sampling point."""
from pydantic import BaseModel


class SamplePoint(BaseModel):
    """The points were laid out using British National Grid, on a 30 metre grid. The
    eastings and northings are the coordinates on the grid."""
    id: int
    description: str
    eastings: int
    northings: int
    latitude: float
    longitude: float
    os_grid_ref: str
