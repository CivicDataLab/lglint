import pandas as pd

from scripts.Constants import METADATA
from scripts.task import Task


class SampleNCases(Task):
    def __init__(self, number_of_cases: int):
        super().__init__()
        self.number_of_cases = number_of_cases

    def _execute(self):
        metadata = self.shared_resources[METADATA]
        assert isinstance(metadata, pd.DataFrame)
        filtered_df = metadata.sample(self.number_of_cases)
        self.share_next(key=METADATA, resource=filtered_df)

