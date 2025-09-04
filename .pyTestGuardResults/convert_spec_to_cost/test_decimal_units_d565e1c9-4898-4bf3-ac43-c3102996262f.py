import unittest
from beancount.core import amount
from beancount.core import position
from beancount.core.number import MISSING
from decimal import Decimal

class ConvertSpecToCostTest(unittest.TestCase):

    def test_decimal_units(self):
            units = amount.Amount(Decimal('10.5'), 'USD')
            cost_spec = (Decimal('1'), Decimal('40'), 'USD', None, None, False)
            cost = convert_spec_to_cost(units, cost_spec)
            self.assertEqual(cost.number, Decimal('4.809523809523809523809523809'))
            self.assertEqual(cost.currency, 'USD')

if __name__ == '__main__':
    unittest.main()
