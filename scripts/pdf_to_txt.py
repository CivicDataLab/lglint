import os

import pdftotext

from scripts.task import Task


class Pdf2Txt(Task):

    def __init__(self, input_dir, output_dir):
        super().__init__()
        self.output_dir = output_dir
        self.input_dir = input_dir

    def execute(self):
        for filename in os.listdir(self.input_dir):
            if filename.endswith(".pdf"):
                ofile = filename.split(".")[0] + ".txt"
                if self.output_dir:
                    ofile = os.path.join(self.output_dir, ofile)
                ifile = os.path.join(self.input_dir, filename)
                with open(ifile, "rb") as input_file:
                    try:
                        pdf = pdftotext.PDF(input_file, "UTF-8")
                        with open(ofile, "w+") as out_file:
                            text = "".join(pdf)
                            out_file.write(text)
                    except pdftotext.Error:
                        print('the file {} looks corrupted'.format(ifile))
