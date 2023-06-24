"""Iterate through a survey data file."""


class SurveyFileReader:
    """Iterate through a survey data file."""
    
    def __init__(self, file_path):
        """Initialize with the survey file path."""
        self.file_path = file_path
        self.file = open(file_path, 'r')
        self.current_record = None
        self.next_record = None

    def __iter__(self):
        return self

    def __next__(self):
        """Return the next record in the file."""
        if self.current_record is None:
            self.current_record = self._read_record()

        record = self.current_record
        if record is None:
            self.file.close()
            raise StopIteration

        self.current_record = self.next_record
        self.next_record = None
        return record

    def _read_record(self):
        """Read from the file to the end of the species list."""
        record_lines = []
        species_found = False  # The species list is the last field in the record.
        for line in self.file:
            # The species list is the last field in the record.
            field_name, _ = line.strip().split(',', 1)
            if field_name.strip() == 'species':
                record_lines.append(line.rstrip())
                species_found = True
            elif species_found:
                if field_name.strip():  # then we are on to the next record.
                    self.next_record = '\n'.join(record_lines)
                    break
                else:
                    record_lines.append(line.rstrip())
            # Append the other lines to the record.
            else:
                record_lines.append(line.rstrip())

        if record_lines:
            return '\n'.join(record_lines)

        self.file.close()
        return None


    def _read_record_wrong(self):
        record_lines = []
        species_found = False
        for line in self.file:
            line = line.rstrip()
            field_name, _ = line.strip().split(',', 1)

            record_lines.append(line)

            if field_name.strip() == 'species':
                record_lines.append(line)
                species_found = True
            elif species_found:
                if field_name.strip() == 'quadrat':
                    self.next_record = line
                    return '\n'.join(record_lines)
                else:
                    record_lines.append(line)

        if record_lines:
            return '\n'.join(record_lines)

        self.file.close()
        return None
