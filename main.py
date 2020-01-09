import os

from scripts.ConcatenateMetadataOfState import ConcatenateMetaDataOfState
from scripts.CopyFilteredJudgements import CopyFilteredJudgements
from scripts.FilterByCaseType import FilterByCaseType
from scripts.Pdf2Txt import Pdf2Txt
from scripts.SampleNCases import SampleNCases
from scripts.pipeline import Pipeline

pipeline = Pipeline()

pipeline \
    .add(ConcatenateMetaDataOfState(base_data_dir="/home/dc/Documents/civicdatalab/judiciary/data/pocso/",
                                    state='Delhi',
                                    out_file='delhi_metadata.csv')) \
    .add(FilterByCaseType(case_type=['SC', 'Cr. Case', 'CC'])) \
    .add(SampleNCases(number_of_cases=30)) \
    .add(CopyFilteredJudgements(source='/home/dc/Documents/civicdatalab/judiciary/data/pocso/', destination=os.path.join(os.path.dirname(__file__), 'input'))) \
    .add(Pdf2Txt(os.path.join(os.path.dirname(__file__), 'input'), os.path.join(os.path.dirname(__file__), 'out')))

pipeline.execute()
