"""
Script for converting pocso case pdfs to text files

Usage:
    pdf2txt.py --idir=<id> [--odir=<od>] [--enc=<e>]

Options:
    --idir=<id>     Provide input directory that has all pdfs
    --odir=<od>     Provide output directory that should have the output files
    --enc=<e>       Provide the required encoding. By default it is UTF-8
"""
from docopt import docopt
import subprocess
import os
import pdftotext

if __name__ == "__main__":
    args = docopt(__doc__)

    idir = args["--idir"]

    odir = args["--odir"]
    for filename in os.listdir(idir):
        if filename.endswith(".pdf"):
            ofile = filename.split(".")[0] + ".txt"
            if odir:
                ofile = odir + ofile
            ifile = idir + filename
            with open(ifile, "rb") as input_file:
                try:
                    pdf = pdftotext.PDF(input_file, "UTF-8")
                except pdftotext.Error:
                    print("the file " + ifile + " looks corrupted")
                    pass
            with open(ofile, "w+") as out_file:
                text = "".join(pdf)
                out_file.write(text)
#            subprocess.call(['pdftotext', '-enc', 'UTF-8',  ifile, ofile])
