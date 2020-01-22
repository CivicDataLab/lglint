import os

import pandas as pd

from scripts.Constants import METADATA
from scripts.task import Task


class AddTitleGeoCNRToFirstLine(Task):

    def __init__(self, input_dir: str):
        super().__init__()
        self.input_dir = input_dir

    def _execute(self):
        metadata = self.shared_resources[METADATA]
        assert isinstance(metadata, pd.DataFrame)
        for filename in os.listdir(self.input_dir):
            if filename.endswith(".txt"):
                judgement = os.path.join(self.input_dir, filename)
                case_number = filename.split('_')[0]
                case = metadata[metadata['case_no'] == int(case_number)]
                title = self._get_case_title(case)
                with open(judgement, "r+") as input_file:
                    judgement = input_file.read()
                    input_file.seek(0)
                    input_file.write("{} ||| {}".format(title, judgement))
                    input_file.truncate()

    @staticmethod
    def _get_case_title(case):
        CNR = case['cino'].item()
        petitioner = case['petparty_name'].item()
        respondent = case['resparty_name'].item()
        court = case['court_name'].item()

        return "{} - {} vs {} - {}".format(CNR, petitioner, respondent, court)
