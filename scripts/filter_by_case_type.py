import pandas as pd

from scripts.task import Task


class FilterByCaseType(Task):
    """
    :case_types: List of case types to be filtered
    """
    case_types: list

    def __init__(self, case_types: list):
        super().__init__()
        self.case_types = case_types

    def execute(self):
        assert isinstance(self.shared_resource, pd.DataFrame)
        filtered_df = self.shared_resource[self.shared_resource['type_name'].isin(self.case_types)]
        self.share_next(filtered_df)
