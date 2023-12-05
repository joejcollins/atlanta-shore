""" Representation of a set of site records. """


class SurveyRecords(object):
    def __init__(self, survey_file_path) -> None:
        """ """
        super().__init__()
        self._survey_file_path = survey_file_path
        # with open(survey_file_path, newline='') as survey_file:
