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

    def test_multiple_entries(self):
            """Test with a mix of different entry types."""
            open_entry = Open(data.new_metadata('filename', 1),
                               data.create_date(2023, 1, 1),
                               'Assets:Bank',
                               ['USD'], None)
            txn = Transaction(
                data.new_metadata('filename', 2),
                data.create_date(2023, 1, 2),
                '*',
                'Description',
                data.EMPTY_SET,
                [],
            )
            posting1 = Posting('Assets:Bank', amount.Amount(100, 'USD'), None, None, None)
            posting2 = Posting('Expenses:Food', amount.Amount(-100, 'USD'), None, None, None)
            txn.postings = [posting1, posting2]
            entries = [open_entry, txn]
            result = postings_by_account(entries)
            self.assertEqual(len(result), 2)
            self.assertEqual(len(result['Assets:Bank']), 2)
            self.assertEqual(result['Assets:Bank'][0], open_entry)
            self.assertIsInstance(result['Assets:Bank'][1], TxnPosting)
            self.assertEqual(len(result['Expenses:Food']), 1)
            self.assertIsInstance(result['Expenses:Food'][0], TxnPosting)

if __name__ == '__main__':
    unittest.main()
