"""
Script for converting text files to jsonl format (the desired format for cheyyali)

Usage:
    converter.py --idir=<id> [--odir=<od>]

Options:
    --idir=<id>     Provide input directory that has all pdfs
    --odir=<od>     Provide output directory that should have the output files
"""
from typing import Dict
from docopt import docopt
import json
import os
from lglint.transformers import convert_to_cheyyali_format


if __name__ == "__main__":
    args = docopt(__doc__)

    idir = args["--idir"]

    odir = args["--odir"]
    for filename in os.listdir(idir):
        if filename.endswith(".txt"):
            ofile = filename.split(".")[0] + ".txt"
            if odir:
                ofile = odir + ofile
            ifile = idir + filename
            with open(ifile, "r") as input_file:
                input_data = input_file.read()
                cheyalli_data = convert_to_cheyyali_format(input_data)
            with open(ofile, "w+") as f:
                f.write(json.dumps(cheyalli_data))
