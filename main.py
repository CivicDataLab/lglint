"""
Module to create and run pipeline for pocso judgement processing for HAQ
"""
import os

from config import settings
from scripts.add_title_geo_and_CNR_to_first_line import AddTitleGeoCNRToFirstLine
from scripts.concatenate_metadata_of_state import ConcatenateMetaDataOfState
from scripts.convert_to_cheyyali_format import ConvertToCheyyaliFormat
from scripts.copy_filtered_judgements import CopyFilteredJudgements
from scripts.filter_by_case_type import FilterMetaDataByCaseType
from scripts.pdf_to_txt import Pdf2Txt
from scripts.pipeline import Pipeline
from scripts.sample_n_cases import SampleNCases

pipeline = Pipeline()

all_judgements_pdf_directory = os.path.join(os.path.dirname(__file__), settings.all_judgements_pdf_directory)
all_judgements_txt_directory = os.path.join(os.path.dirname(__file__), settings.all_judgements_txt_directory)
pipeline \
    .add(ConcatenateMetaDataOfState(base_data_dir=settings.base_data_dir,
                                    state=settings.state_to_analyse,
                                    out_file=settings.combined_metadata_file)) \
    .add(FilterMetaDataByCaseType(case_types=settings.judgements_case_types)) \
    .add(SampleNCases(number_of_cases=settings.number_of_sample_judgements)) \
    .add(CopyFilteredJudgements(source=settings.base_data_dir,
                                destination=all_judgements_pdf_directory)) \
    .add(Pdf2Txt(all_judgements_pdf_directory, all_judgements_txt_directory)) \
    .add(AddTitleGeoCNRToFirstLine(input_dir=all_judgements_txt_directory,
                                pattern=r'(.*)_\d\.txt')) \
    .add(ConvertToCheyyaliFormat(input_dir=all_judgements_txt_directory,
                                out_file=settings.final_cheyyali_judgements,
                                pattern=r'(.*)_\d\.txt'))

pipeline.execute()
