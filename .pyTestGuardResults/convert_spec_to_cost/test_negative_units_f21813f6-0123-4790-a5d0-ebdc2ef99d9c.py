import unittest
from beancount.core import amount
from beancount.core import position
from beancount.core.number import MISSING
from datetime import date

class TestConvertSpecToCost(unittest.TestCase):

    def test_negative_units(self):
            units = amount.Amount(-10, 'USD')
            cost_spec = (2.0, 5.0, 'CAD', None, None, False)
            cost = convert_spec_to_cost(units, cost_spec)
            self.assertEqual(cost.number, 1.5)
            self.assertEqual(cost.currency, 'CAD')

if __name__ == '__main__':
    unittest.main()
