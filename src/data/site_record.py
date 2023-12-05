# import io


class SiteRecord(object):
    def __init__(self, site_record_string) -> None:
        """Initialize the site record attributes."""
        super().__init__()
        self.quadrat = None
        self.waypoint = None
        self.grid_reference = None
        self.photo_up = None
        self.photo_down = None
        self.wetness = None
        self.canopy = None
        # self.species = []
        # string_as_file = io.StringIO(site_record_string)
        # self._initialize_attributes()

    def _initialize_attributes(self, string_as_file):
        """Set the site record values"""
        for row in string_as_file:
            first = row[0]
            second = row[1]
            third = row[3]
            match first:
                case "quadrat":
                    self.quadrat = {"id": second, "comment": third}
                case "waypoint":
                    self.waypoint = {"name": second, "comment": third}
