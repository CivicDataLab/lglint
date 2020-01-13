import json
import os
from typing import List, Dict, Mapping

from scripts.task import Task


class ConvertToCheyyaliFormat(Task):

    def __init__(self, input_dir: str, out_file: str):
        super().__init__()
        self.out_file = out_file
        self.input_dir = input_dir

    def execute(self):
        for filename in os.listdir(self.input_dir):
            if filename.endswith(".txt"):
                judgement = os.path.join(self.input_dir, filename)
                with open(judgement, "r") as input_file:
                    input_data = input_file.read()
                    cheyalli_data = self._convert_to_cheyyali_format(input_data)
                    cheyyali_file = os.path.join(self.input_dir, self.out_file)
                    with open(cheyyali_file, "a") as f:
                        f.writelines([json.dumps(cheyalli_data) + '\n'])

    @staticmethod
    def _convert_to_cheyyali_format(input_text) -> Dict[str, Mapping[str, List[List[str]]]]:
        return {'text': input_text, "labels": []}
