import pandas as pd

from scripts.Constants import METADATA
from scripts.task import Task


class FilterMetaDataByCaseType(Task):
    """
    :case_types: List of case types to be filtered
    """
    case_types: list

    def __init__(self, case_types: list):
        super().__init__()
        self.case_types = case_types

    def _execute(self):
        metadata = self.shared_resources[METADATA]
        assert isinstance(metadata, pd.DataFrame)
        filtered_df = metadata[metadata['type_name'].isin(self.case_types)]
        
        self.share_next(key=METADATA, resource=filtered_df)