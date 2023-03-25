# bookkeeping-beancount

Step 0:
Prepare your transaction history in `beancount/raw/` directory.

Step 1:
Run following CLI in your teminal to set catogories for your transactions.
```
$ cd <your repo>
$ python3 repo/beancount_importers/run.py beancount/
```

Step 2:
All transaction with assigned categories will be shown in `beancount/raw/journal/imported-txns.beancount`.

Run following CLI in your terminal to track your transactions with Fava.
```
$ cd <your repo>
$ fava beancount/raw/journal/all.beancount
```