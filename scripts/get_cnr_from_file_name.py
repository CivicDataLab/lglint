import os
import re

from scripts.Constants import CNR_LIST
from scripts.task import Task


class GetCNRFromPdf(Task):

    def __init__(self, data_dir: str, file_format: str, cnr_pattern: str):
        super().__init__()
        self.data_dir = data_dir
        self.file_format = file_format
        try:
            self.cnr_pattern = re.compile(cnr_pattern)
        except re.error:
            raise Exception({"message": "given pattern invalid"})

    def _execute(self):
        cnr_list = []

        for filename in os.listdir(self.data_dir):
            if filename.endswith(self.file_format) and re.search(self.cnr_pattern, filename):
                cnr_list.append(re.findall(self.cnr_pattern, filename)[0])

        self.share_next(CNR_LIST, cnr_list)
