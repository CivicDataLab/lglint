import os

import pandas as pd

from scripts.task import Task


class LoadMetaData(Task):
    def __init__(self, base_data_dir: str, metadata: str):
        super().__init__()
        self.base_data_dir = base_data_dir
        self.metadata = metadata

    def _execute(self):
        metadata = pd.read_csv(os.path.join(self.base_data_dir, self.metadata))
        self.share_next(metadata)