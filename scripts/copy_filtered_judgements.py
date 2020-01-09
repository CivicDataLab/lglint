import os
from shutil import copyfile

import pandas as pd

from scripts.task import Task


class CopyFilteredJudgements(Task):
    def __init__(self, source: str, destination: str):
        super().__init__()
        self.source = source
        self.destination = destination

    def execute(self):
        assert isinstance(self.shared_resource, pd.DataFrame)
        case_numbers = self.shared_resource['case_no'].tolist()
        # for ci in case_numbers:
        for root, dirs, files in os.walk(self.source):
            for file in files:
                if file.endswith('.pdf') and case_numbers.__contains__(file.split('_')[0]):
                    path_file = os.path.join(self.destination, file)
                    copyfile(os.path.join(root, file), path_file)
