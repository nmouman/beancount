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

class PostingsByAccountTest(unittest.TestCase):

    def test_balance_entry(self):
            """Test with a single Balance entry."""
            balance_entry = Balance(data.new_metadata('filename', 1),
                                    data.create_date(2023, 1, 1),
                                    'Assets:Bank',
                                    amount.Amount(100, 'USD'), None)
            entries = [balance_entry]
            result = postings_by_account(entries)
            self.assertEqual(len(result), 1)
            self.assertEqual(result['Assets:Bank'][0], balance_entry)

if __name__ == '__main__':
    unittest.main()
