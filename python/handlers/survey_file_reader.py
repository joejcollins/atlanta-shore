"""Iterate through a survey data file."""

class SurveyFileReader:
    """"""
    
    def __init__(self, file_path):
        """Initialize with the survey file path."""
        self.file_path = file_path
        self.file = open(file_path, 'r')
        self.current_record = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_record is None:
            self.current_record = self._read_record()

        record = self.current_record
        if record is None:
            self.file.close()
            raise StopIteration

        self.current_record = None  # Reset current record for the next iteration
        return record

    def _read_record(self):
        record_lines = []
        species_found = False
        for line in self.file:
            field_name, field_value = line.strip().split(',', 1)

            if field_name.strip() == 'species':
                record_lines.append(line.rstrip())
                species_found = True
            elif species_found:
                if field_name.strip():
                    self.current_record = f'{field_name},{field_value}'
                    break
                else:
                    record_lines.append(line.rstrip())

        if record_lines:
            return '\n'.join(record_lines)

        self.file.close()
        return None
