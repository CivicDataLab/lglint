import os

from config import settings
from scripts.add_title_geo_and_CNR_to_first_line import AddTitleGeoCNRToFirstLine
from scripts.convert_to_cheyyali_format import ConvertToCheyyaliFormat
from scripts.copy_filtered_judgements import CopyFilteredJudgements
from scripts.filter_by_cnr import FilterMetaDataByCNR
from scripts.get_cnr_from_file_name import GetCNRFromPdf
from scripts.load_meta_data import LoadMetaData
from scripts.pdf_to_txt import Pdf2Txt
from scripts.pipeline import Pipeline

all_judgements_pdf_directory = os.path.join(os.path.dirname(__file__), settings.all_judgements_pdf_directory)
all_judgements_txt_directory = os.path.join(os.path.dirname(__file__), settings.all_judgements_txt_directory)

pipeline = Pipeline()

pipeline \
    .add(GetCNRFromPdf(data_dir=all_judgements_pdf_directory,
                       file_format="pdf",
                       cnr_pattern=r".* - (.*)\.pdf")) \
    .add(LoadMetaData(base_data_dir=settings.base_data_dir,
                      metadata=settings.combined_metadata_file)) \
    .add(FilterMetaDataByCNR(cnr_list=[])) \
    .add(Pdf2Txt(all_judgements_pdf_directory, all_judgements_txt_directory)) \
    .add(AddTitleGeoCNRToFirstLine(input_dir=all_judgements_txt_directory,
                                   pattern=r'.* - (.*)\.txt',
                                   use_cnr=True)) \
    .add(ConvertToCheyyaliFormat(input_dir=all_judgements_txt_directory,
                                 out_file=settings.final_cheyyali_judgements,
                                 pattern=r'.* - (.*)\.txt',
                                 use_cnr=True))

pipeline.execute()
