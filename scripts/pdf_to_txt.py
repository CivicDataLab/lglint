import os

import pdftotext

from scripts.task import Task

FOOTER_PATTERN = r"(.* No\. .* Vs\. .* Page No\.\d of \d+)"


class Pdf2Txt(Task):

    def __init__(self, input_dir, output_dir):
        super().__init__()
        self.output_dir = output_dir
        self.input_dir = input_dir

    def execute(self):
        for filename in os.listdir(self.input_dir):
            if filename.endswith(".pdf"):
                out_file = filename.split(".")[0] + ".txt"
                if self.output_dir:
                    out_file = os.path.join(self.output_dir, out_file)
                in_file = os.path.join(self.input_dir, filename)
                with open(in_file, "rb") as input_file:
                    try:
                        pdf = pdftotext.PDF(input_file, "UTF-8")
                        text = ""
                        with open(out_file, "w+") as out_file:
                            for page in pdf:
                                text += self._remove_footer(filename, page)
                                # text = "".join(pdf)  # Join all the pages
                            out_file.write(text)
                    except pdftotext.Error:
                        print('the file {} looks corrupted'.format(in_file))


    @staticmethod
    def _remove_footer(filename, page):
        # if re.search(FOOTER_PATTERN, page):
        #     return re.sub(FOOTER_PATTERN, "", page)
        # else:
        #     raise Exception({'page': page, 'file': filename})
        if page.split('\n')[-1] == "":
            return "\n".join(page.split('\n')[0:-2])
        else:
            raise Exception({'page': page, 'file': filename})
