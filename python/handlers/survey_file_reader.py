"""Iterate through a survey data file."""
from typing import Optional


class SurveyFileReader:
    """Iterate through a survey data file."""

    def __init__(self, file_path: str) -> None:
        """Initialize with the survey file path."""
        # Open the file on initialization and ensure that there are no records yet.
        self.file = open(file_path, "r")
        self.current_record = None
        self.next_line = None  # So we can read ahead.

    def __iter__(self):
        return self

    def __next__(self) -> str:
        """Return the next record in the file."""
        # If there is no record go and get it.
        if self.current_record is None:
            self.current_record = self._read_record()
        # Create a record to return or stop.
        record = self.current_record
        if record is None:  # we are at the end of the file.
            self.file.close()
            raise StopIteration
        self.current_record = None  # Reset current record for the next iteration
        return record

    def _read_record(self) -> Optional[str]:
        """Read from the file to the end of the species list."""
        record_lines = ""
        species_found = False  # The species list is the last field in the record.
        # If there is a line from the next record, add it to the record lines.
        if self.next_line and self._field_name(self.next_line):
            record_lines += self.next_line
        for line in self.file:
            self.next_line = line  # Keep line in case it's needed for next record.
            # The species list is the last field in the record.
            field_name = self._field_name(line)
            if field_name == "species":
                record_lines += line
                species_found = True
            elif species_found:
                if field_name:  # then we are on to the next record
                    break
                else:  # Append another species line.
                    record_lines += line
            # Append the other lines to the record.
            else:
                record_lines += line
        # Return the lines or close and finish.
        if record_lines:
            return record_lines
        self.file.close()
        return None

    def _field_name(self, line):
        """Return the field name from the line."""
        field_name, _ = line.split(",", 1)
        field_name = field_name.strip()
        return field_name
