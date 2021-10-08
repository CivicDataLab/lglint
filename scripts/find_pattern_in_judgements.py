import os
import re

import pandas as pd

from scripts.task import Task

from Constants import METADATA, RESULT


class FindPatternInJudgements(Task):

    def __init__(self, input_dir: str, pattern: str, label: str, line_limit: int = 0, limit_lines: bool = False,
                 store_result: bool = True):
        super().__init__()
        self.limit_lines = limit_lines
        self.line_limit = line_limit
        self.store_result = store_result
        self.label = label
        self.input_dir = input_dir
        try:
            self.pattern = re.compile(pattern, re.IGNORECASE)
        except re.error:
            raise Exception({"message": "given pattern invalid"})

    def _execute(self):
        # metadata = self.shared_resources.get(METADATA, None)
        # assert isinstance(metadata, pd.DataFrame)
        labels_found = self.shared_resources.get(RESULT, {})
        for filename in os.listdir(self.input_dir):
            if filename.endswith(".txt"):
                judgement = os.path.join(self.input_dir, filename)
                cino = filename.split('_')[0]
                results = []
                line_count = 0
                with open(judgement) as f:
                    for line in f:
                        line = self.clean_line(line)
                        if not self.line_limit or line_count <= self.line_limit:
                            all_found = self.get_patterns(line)
                            if self.label == "fine_imposed":
                                for found in all_found:
                                    results.append(found.replace(',', ""))
                            else:
                                results.extend(all_found)
                            line_count += 1
                if not self.store_result:
                    results = True if len(results) else False
                else:
                    current = labels_found.get(cino, {self.label: []}).get(self.label, [])
                    results = current + results
                labels_found.setdefault(cino, {}).update({self.label: results})
        self.share_next(RESULT, labels_found)

    def get_patterns(self, line):
        patterns = []
        all_found = self.pattern.findall(line)
        for found in all_found:
            if type(found) is tuple:
                filtered_list = list(filter(None, list(found)))
                patterns.extend(filtered_list)
            else:
                patterns.append(found)
        return list(set(patterns))

    @staticmethod
    def clean_line(line):
        return line.\
            replace("\n", ' ').\
            replace('  ', ' ')
