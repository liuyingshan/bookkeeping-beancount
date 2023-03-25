from beancount.ingest.importers import csv
from beancount.ingest.importers.csv import Col
import re

class Importer(csv.Importer):
    '''
    Importer for the UOB ONE credit card txns csv.
    '''

    def __init__(self, self_account):
        super().__init__(
            {Col.DATE: 0,
             Col.NARRATION: 2,
             Col.AMOUNT: 6},
            self_account,
            'SGD',
            invert_sign=True
        )

        
    def identify(self, file):
        return  re.match(r".*UOB_CC_.*csv", file.name) != None
