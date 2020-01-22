import pandas as pd

from scripts.Constants import METADATA
from scripts.task import Task


class FilterMetaDataByCNR(Task):

    def __init__(self, cnr_list: list):
        super().__init__()
        self.cnr_list = cnr_list

    def _execute(self):
        metadata = self.shared_resources[METADATA]
        assert isinstance(metadata, pd.DataFrame)
        filtered_list = metadata[metadata['cino'].isin(self.cnr_list)]
        self.share_next(key=METADATA, resource=filtered_list)
