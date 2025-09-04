import unittest
import collections
from beancount.core import data
from beancount.core import amount
from beancount.core import account
from beancount.core.data import Transaction, Posting, Open, Close, Balance, Note, Document, Pad, Custom, TxnPosting
from beancount.core import position

class PostingsByAccountTest(unittest.TestCase):

    def test_pad_entry(self):
            pad_directive = data.Pad(
                data.SourcePos("test", 1, 1, ""), data.Date(2023, 1, 1), "Assets:Bank", "Expenses:Food"
            )
            entries = [pad_directive]
            result = postings_by_account(entries)
            self.assertEqual(len(result), 2)
            self.assertIn("Assets:Bank", result)
            self.assertIn("Expenses:Food", result)
            self.assertEqual(len(result["Assets:Bank"]), 1)
            self.assertEqual(len(result["Expenses:Food"]), 1)
            self.assertIsInstance(result["Assets:Bank"][0], data.Pad)
            self.assertIsInstance(result["Expenses:Food"][0], data.Pad)
            self.assertEqual(result["Assets:Bank"][0], pad_directive)
            self.assertEqual(result["Expenses:Food"][0], pad_directive)

if __name__ == '__main__':
    unittest.main()
