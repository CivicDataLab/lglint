import os

from simple_config import Config

default_settings = {
    "base_data_dir": '/path/to/base_data_dir',
    'state_to_analyse': 'state name',
    'number_of_sample_judgements': 30,
    'judgements_case_types': ['case_type'],
    'combined_metadata_file': 'metadata.csv',
    "all_judgements_pdf_directory": "input",
    "all_judgements_txt_directory": "output",
    "final_cheyyali_judgements": "cheyyali_judgements.json",
    "cnr_list": ['cnr_num']
}
config_file = os.path.join(os.path.dirname(__file__), 'config.json')
settings = Config(config_file, defaults=default_settings)
