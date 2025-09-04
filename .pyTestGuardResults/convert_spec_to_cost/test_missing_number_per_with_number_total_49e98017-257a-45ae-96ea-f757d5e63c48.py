import unittest
from beancount.core import amount
from beancount.core import position
from beancount.core.number import MISSING, ZERO
from datetime import date

class ConvertSpecToCostTest(unittest.TestCase):

    def test_missing_number_per_with_number_total(self):
            units = amount.Amount(10, 'USD')
            cost_spec = (MISSING, 2.3, 'EUR', date(2023, 1, 1), 'label', False)
            cost = convert_spec_to_cost(units, cost_spec)
            self.assertEqual(cost.number, 0.23)
            self.assertEqual(cost.currency, 'EUR')
            self.assertEqual(cost.date, date(2023, 1, 1))
            self.assertEqual(cost.label, 'label')

if __name__ == '__main__':
    unittest.main()
