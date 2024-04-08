"""Static parameters for the whole site."""

from pydantic import BaseModel


class Site(BaseModel):
    """Site parameters."""

    area: float  # Area of the site in hectares.
    fence_length: float  # Length of the fence in metres.
