from scripts.task import Task


class FilterMetaDataByCNR(Task):

    def __init__(self, cnr_list: list):
        super().__init__()
        self.cnr_list = cnr_list

    def _execute(self):
        filtered_list = self.shared_resource[self.shared_resource['cino'].isin(self.cnr_list)]
        self.share_next(filtered_list)
