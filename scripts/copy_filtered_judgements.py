"""
Task to copy the filtered judgements to common place for further processing
"""
import os
from shutil import copyfile

import pandas as pd

from scripts.Constants import METADATA
from scripts.task import Task


class CopyFilteredJudgements(Task):
    def __init__(self, source: str, destination: str):
        super().__init__()
        self.source = source
        self.destination = destination

    def _execute(self):
        metadata = self.shared_resources[METADATA]
        assert isinstance(metadata, pd.DataFrame)
        # case_numbers = metadata['case_no'].tolist()
        # for ci in case_numbers:
        for root, dirs, files in os.walk(self.source):
            for file in files:
                if file.endswith('.pdf'):
                    try:
                        # if '_' in file and int(file.split('_')[0]) in case_numbers:
                        if '_' in file and 'Judgment' in file:
                            path_file = os.path.join(self.destination, file)
                            copyfile(os.path.join(root, file), path_file)
                    except Exception as e:
                        print(e.__str__() + "for file" + root + '/' + file)
