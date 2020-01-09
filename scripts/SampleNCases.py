import pandas as pd

from scripts.task import Task


class SampleNCases(Task):
    def __init__(self, number_of_cases: int):
        super().__init__()
        self.number_of_cases = number_of_cases

    def execute(self):
        assert isinstance(self.shared_resource, pd.DataFrame)
        filtered_df = self.shared_resource.sample(self.number_of_cases)
        self.share_next(filtered_df)
