import json
import os

import pandas

from scripts.task import Task


class ConcatenateMetaDataOfState(Task):

    def __init__(self, base_data_dir: str, state: str, out_file: str):
        super().__init__()
        self.out_file = out_file
        self.state = state
        self.base_data_dir = base_data_dir

    def execute(self):
        metadata = []
        for root, dirs, files in os.walk(self.base_data_dir + self.state):
            for file in files:
                if file.endswith('.json'):
                    path_file = os.path.join(root, file)
                    with open(path_file) as f:
                        data = json.load(f)
                        metadata.append(data)
        df = pandas.DataFrame.from_records(metadata).fillna(0)
        self.share_next(df)
        df.to_csv(self.base_data_dir + self.out_file, index=False)
