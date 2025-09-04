import unittest
from beancount.core import amount
from beancount.core import position
from beancount.core.number import MISSING
from decimal import Decimal

class ConvertSpecToCostTest(unittest.TestCase):

    def test_units_not_amount(self):
            cost_spec = (Decimal('1.23'), None, 'EUR', None, None, False)
            units = 10
            cost = convert_spec_to_cost(units, cost_spec)
            self.assertEqual(units, 10)

if __name__ == '__main__':
    unittest.main()
