#!/usr/bin/env python3

import glob
import os
import json
import sys

from importers.dbs_acc import dbs_acc_csv
from importers.uob_acc import uob_acc_csv
from importers.uob_cc import uob_cc_csv
from importers.ocbc_acc import ocbc_acc_csv

def run_reconcile(beancount_root, extra_args):
    import beancount_import.webserver

    journal_dir = os.path.join(beancount_root, 'journal')
    data_dir = os.path.join(beancount_root, 'raw')

    data_sources = [
        # DBS Bank Account
        dict(
            module='beancount_import.source.generic_importer_source',
            importer=dbs_acc_csv.Importer("Assets:Bank:Dbs"),
            account="Assets:Bank:Dbs",
            directory=data_dir
        ),
        # UOB Bank Account
        dict(
            module='beancount_import.source.generic_importer_source',
            importer=uob_acc_csv.Importer("Assets:Bank:Uob"),
            account="Assets:Bank:Uob",
            directory=data_dir
        ),
        # UOB Credit Card
        dict(
            module='beancount_import.source.generic_importer_source',
            importer=uob_cc_csv.Importer("Liabilities:Bank:Uob"),
            account="Liabilities:Bank:Uob",
            directory=data_dir
        ),
        # OCBC Bank Account
        dict(
            module='beancount_import.source.generic_importer_source',
            importer=ocbc_acc_csv.Importer("Assets:Bank:Ocbc"),
            account="Assets:Bank:Ocbc",
            directory=data_dir
        ),
    ]

    beancount_import.webserver.main(
        extra_args,
        journal_input=os.path.join(journal_dir, 'all.beancount'),
        ignored_journal=os.path.join(journal_dir, 'ignored.beancount'),
        default_output=os.path.join(journal_dir, 'imported-txns.beancount'),
        open_account_output_map=[
            ('.*', os.path.join(journal_dir, 'accounts.beancount')),
        ],
        balance_account_output_map=[
            ('.*', os.path.join(journal_dir, 'accounts.beancount')),
        ],
        price_output=os.path.join(journal_dir, 'prices.beancount'),
        data_sources=data_sources,
    )

if __name__ == '__main__':
    run_reconcile(sys.argv[1], sys.argv[2:])
