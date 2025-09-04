import unittest
from beancount.core import amount
from beancount.core import position
from beancount.core.number import MISSING
from datetime import date

class ConvertSpecToCostTest(unittest.TestCase):

    def test_no_cost_spec(self):
            units = amount.Amount(10, 'USD')
            self.assertIsNone(convert_spec_to_cost(units, None))

if __name__ == '__main__':
    unittest.main()
