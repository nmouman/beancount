import unittest
import collections
from beancount.core import account
from beancount.core import amount
from beancount.core import data
from beancount.core import inventory
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
from beancount.core import number
from decimal import Decimal

class PostingsByAccountTest(unittest.TestCase):

    def test_custom_entry(self):
            custom_entry = Custom(
                data.SourcePos("test", 1, 1, "test"),
                data.create_date(2023, 1, 1),
                "test",
                [data.CustomValue("Assets:Bank", data.TYPE_ACCOUNT)],
                data.EMPTY_DICT,
            )
            entries = [custom_entry]
            result = postings_by_account(entries)
            self.assertEqual(len(result), 1)
            self.assertEqual(result["Assets:Bank"][0], custom_entry)

if __name__ == '__main__':
    unittest.main()
