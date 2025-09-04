import unittest
import collections
from beancount.core import account
from beancount.core import amount
from beancount.core import data
from beancount.core.data import Balance
from beancount.core.data import Close
from beancount.core.data import Custom
from beancount.core.data import Document
from beancount.core.data import Note
from beancount.core.data import Open
from beancount.core.data import Pad
from beancount.core.data import Posting
from beancount.core.data import Transaction
from beancount.core.data import TxnPosting
from beancount.core import flags
from beancount.core import position
from beancount.core import number

class PostingsByAccountTest(unittest.TestCase):

    def test_transaction_entry(self):
            txn = Transaction(
                data.SourcePos("test", 1, 1, "test"),
                data.create_date(2023, 1, 1),
                flags.FLAG_OKAY,
                "Payee",
                "Narration",
                data.EMPTY_SET,
                data.EMPTY_DICT,
                [
                    Posting("Assets:Bank", amount.Amount(number.D("10"), "USD"), None, None, None),
                    Posting("Expenses:Food", amount.Amount(number.D("-10"), "USD"), None, None, None),
                ],
            )
            entries = [txn]
            result = postings_by_account(entries)
            self.assertEqual(len(result), 2)
            self.assertIsInstance(result["Assets:Bank"][0], TxnPosting)
            self.assertEqual(result["Assets:Bank"][0].txn, txn)
            self.assertEqual(result["Assets:Bank"][0].posting, txn.postings[0])
            self.assertIsInstance(result["Expenses:Food"][0], TxnPosting)
            self.assertEqual(result["Expenses:Food"][0].txn, txn)
            self.assertEqual(result["Expenses:Food"][0].posting, txn.postings[1])

if __name__ == '__main__':
    unittest.main()
