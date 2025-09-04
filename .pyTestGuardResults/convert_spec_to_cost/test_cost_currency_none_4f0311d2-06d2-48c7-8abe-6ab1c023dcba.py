import unittest
from beancount.core import amount
from beancount.core import position
from beancount.core.number import MISSING
from decimal import Decimal

class ConvertSpecToCostTest(unittest.TestCase):

    def test_cost_currency_none(self):
            units = amount.Amount(Decimal('10'), 'USD')
            cost_spec = (Decimal('1.23'), None, None, None, None, False)
            cost = convert_spec_to_cost(units, cost_spec)
            self.assertEqual(cost.number, Decimal('1.23'))
            self.assertIsNone(cost.currency)

if __name__ == '__main__':
    unittest.main()
