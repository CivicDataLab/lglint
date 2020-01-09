import os

from scripts.concatenate_metadata_of_state import ConcatenateMetaDataOfState
from scripts.copy_filtered_judgements import CopyFilteredJudgements
from scripts.filter_by_case_type import FilterByCaseType
from scripts.pdf_to_txt import Pdf2Txt
from scripts.pipeline import Pipeline
from scripts.sample_n_cases import SampleNCases

pipeline = Pipeline()

pipeline \
    .add(ConcatenateMetaDataOfState(base_data_dir="/home/dc/Documents/civicdatalab/judiciary/data/pocso/",
                                    state='Delhi',
                                    out_file='delhi_metadata.csv')) \
    .add(FilterByCaseType(case_types=['SC', 'Cr. Case', 'CC'])) \
    .add(SampleNCases(number_of_cases=30)) \
    .add(CopyFilteredJudgements(source='/home/dc/Documents/civicdatalab/judiciary/data/pocso/',
                                destination=os.path.join(os.path.dirname(__file__), 'input'))) \
    .add(Pdf2Txt(os.path.join(os.path.dirname(__file__), 'input'), os.path.join(os.path.dirname(__file__), 'out')))

pipeline.execute()
