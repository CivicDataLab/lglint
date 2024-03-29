import os

import re

import pandas as pd

from scripts.Constants import METADATA
from scripts.task import Task
from scripts.util import get_target_case



class AddTitleGeoCNRToFirstLine(Task):


    def __init__(self, input_dir: str, pattern: str, use_cnr: bool = False):
        super().__init__()
        self.use_cnr = use_cnr
        self.input_dir = input_dir
        try:
            self.pattern = re.compile(pattern)
        except re.error:
            raise Exception({"message": "given pattern invalid"})

    def _execute(self):
        metadata = self.shared_resources[METADATA]
        assert isinstance(metadata, pd.DataFrame)
        for filename in os.listdir(self.input_dir):
            if filename.endswith(".txt"):
                judgement = os.path.join(self.input_dir, filename)
                case = get_target_case(filename, metadata, self.use_cnr, self.pattern)
                if case is not None and not case.empty:
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

        return "{} - {} vs {} - {}".format(CNR, petitioner, respondent, court)
        //return "{} - {} vs {} - {} - {} - {} - {}".format(CNR, petitioner, respondent, court, case_number, year, status)

