import os

import pandas as pd

from scripts.task import Task


class AddTitleGeoCNRToFirstLine(Task):

    def __init__(self, input_dir: str):
        super().__init__()
        self.input_dir = input_dir

    def _execute(self):
        assert isinstance(self.shared_resource, pd.DataFrame)
        for filename in os.listdir(self.input_dir):
            if filename.endswith(".txt"):
                judgement = os.path.join(self.input_dir, filename)
                case_number = filename.split('_')[0]
                case = self.shared_resource[self.shared_resource['case_no'] == case_number]
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
        case_number = case['reg_no'].item()
        year = case['reg_year'].item()
        status = 'Pending' if case['disp_nature'].item() == 0 else "Disposed"

        return "{} - {} vs {} - {} - {} - {} - {}".format(CNR, petitioner, respondent, court, case_number, year, status)
