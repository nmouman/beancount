import unittest
import collections
from beancount.core import data
from beancount.core import amount
from beancount.core import account
from beancount.core.data import Transaction
from beancount.core.data import Posting
from beancount.core.data import Open
from beancount.core.data import Close
from beancount.core.data import Balance
from beancount.core.data import Note
from beancount.core.data import Document
from beancount.core.data import Pad
from beancount.core.data import Custom
from beancount.core.data import TxnPosting
from beancount.core import position
from beancount.core import inventory
from beancount.core import flags
from beancount.core import number

class PostingsByAccountTest(unittest.TestCase):

    def test_empty_entries(self):
            entries = []
            result = postings_by_account(entries)
            self.assertEqual(result, {})

if __name__ == '__main__':
    unittest.main()
