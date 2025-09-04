import unittest
from beancount import CostSpec
from beancount.core import amount
from beancount.core import position
from beancount.core.number import MISSING
from decimal import Decimal

class TestConvertSpecToCost(unittest.TestCase):

    def test_valid_cost_spec_with_date_and_label(self):
            units = amount.Amount(Decimal('10'), 'USD')
            cost_spec = CostSpec(Decimal('5'), Decimal('50'), 'EUR', '2023-10-26', 'test_label', False)
            cost = convert_spec_to_cost(units, cost_spec)
            self.assertEqual(cost.number, Decimal('10'))
            self.assertEqual(cost.currency, 'EUR')
            self.assertEqual(cost.date, '2023-10-26')
            self.assertEqual(cost.label, 'test_label')

if __name__ == '__main__':
    unittest.main()
