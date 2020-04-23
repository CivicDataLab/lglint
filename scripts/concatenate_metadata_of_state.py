"""
Class to concatenate the metadata of all the judgements to a single csv file
"""

import json
import os

import pandas

from scripts.Constants import METADATA
from scripts.task import Task


class ConcatenateMetaDataOfState(Task):

    def __init__(self, base_data_dir: str, state: str, out_file: str):
        super().__init__()
        self.out_file = out_file
        self.state = state
        self.base_data_dir = base_data_dir

    def _execute(self):
        """
        Task iterates through all the folders of input directory and creates a CSV file with combined metadata
        """
        metadata = []
        for root, dirs, files in os.walk(self.base_data_dir + self.state):
            for sub_file in files:
                if sub_file.endswith('_parsed.json'):
                    path_file = os.path.join(root, sub_file)
                    with open(path_file) as f:
                        data = json.load(f)
                        metadata.append(data)
        df = pandas.DataFrame.from_records(metadata).fillna(0)
        self.share_next(key=METADATA, resource=df)
        df.to_csv(self.base_data_dir + self.out_file, index=False)
