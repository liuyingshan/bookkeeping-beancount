from beancount.ingest.importers import csv
from beancount.ingest.importers.csv import Col
import re

class Importer(csv.Importer):
    '''
    Importer for the UOB ONE account txns csv.
    '''

    def __init__(self, self_account):
        super().__init__(
            {Col.DATE: 0,
             Col.NARRATION: 1,
             Col.AMOUNT_DEBIT: 2,
             Col.AMOUNT_CREDIT: 3},
            self_account,
            'SGD'
        )

        
    def identify(self, file):
        return  re.match(r".*UOB_ACC_.*csv", file.name) != None
