import unittest
from beancount.core import amount
from beancount.core import position
from beancount.core.number import MISSING
from datetime import date

class TestConvertSpecToCost(unittest.TestCase):

    def test_number_per_zero_number_total_zero(self):
            units = amount.Amount(10, 'USD')
            cost_spec = (0.0, 0.0, 'CAD', None, None, False)
            cost = convert_spec_to_cost(units, cost_spec)
            self.assertEqual(cost.number, 0.0)
            self.assertEqual(cost.currency, 'CAD')

if __name__ == '__main__':
    unittest.main()
