from beancount.ingest.importers import csv
from beancount.ingest.importers.csv import Col
import re

class Importer(csv.Importer):
    '''
    Importer for the DBS Multiplier account txns csv.
    '''

    def __init__(self, self_account):
        super().__init__(
            {Col.DATE: 0,
             Col.NARRATION1: 6,
             Col.NARRATION2: 7,
             Col.NARRATION3: 8,
             Col.AMOUNT_DEBIT: 4,
             Col.AMOUNT_CREDIT: 5},
            self_account,
            'SGD'
        )

        
    def identify(self, file):
        return  re.match(r".*DBS_.*csv", file.name) != None
