import unittest
from beancount.core import amount
from beancount.core import position
from beancount.core.number import MISSING
from decimal import Decimal

class ConvertSpecToCostTest(unittest.TestCase):

    def test_number_per_and_number_total_zero_units(self):
            units = amount.Amount(Decimal('0'), 'USD')
            cost_spec = (Decimal('1.00'), Decimal('2.30'), 'EUR', None, None, False)
            cost = convert_spec_to_cost(units, cost_spec)
            self.assertEqual(cost, None)

if __name__ == '__main__':
    unittest.main()
