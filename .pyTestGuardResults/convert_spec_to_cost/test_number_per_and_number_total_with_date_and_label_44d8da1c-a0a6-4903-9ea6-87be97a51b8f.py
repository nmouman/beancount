import unittest
from beancount.core import amount
from beancount.core import position
from beancount.core.number import MISSING
from datetime import date

class ConvertSpecToCostTest(unittest.TestCase):

    def test_number_per_and_number_total_with_date_and_label(self):
            units = amount.Amount(10, 'USD')
            cost_spec = (1.0, 2.3, 'USD', date(2023, 1, 1), "label", False)
            cost = convert_spec_to_cost(units, cost_spec)
            self.assertEqual(cost.number, 1.23)
            self.assertEqual(cost.currency, 'USD')
            self.assertEqual(cost.date, date(2023, 1, 1))
            self.assertEqual(cost.label, "label")

if __name__ == '__main__':
    unittest.main()
