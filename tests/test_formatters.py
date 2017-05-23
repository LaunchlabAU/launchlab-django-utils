from django.test import TestCase
from launchlab_django_utils.formatters.currency import currency_display
from decimal import Decimal

class CurrencyFormatterTestCase(TestCase):

    def test_nonzero_cents_int(self):
        value = 1234
        self.assertEqual(currency_display(value), '$12.34')

    def test_nonzero_cents_decimal(self):
        value = Decimal('1234')
        self.assertEqual(currency_display(value), '$12.34')

    def test_zero_cents_int_show_complete_true(self):
        value = 1400
        self.assertEqual(currency_display(value, show_complete=True), '$14.00')

    def test_zero_cents_int_show_complete_false(self):
        value = 1400
        self.assertEqual(currency_display(value, show_complete=False), '$14')

    def test_zero_cents_decimal_show_complete_true(self):
        value = Decimal('1400')
        self.assertEqual(currency_display(value, show_complete=True), '$14.00')

    def test_zero_cents_decimal_show_complete_false(self):
        value = Decimal('1400')
        self.assertEqual(currency_display(value, show_complete=False), '$14')

    def test_include_sign_true(self):
        value = 123
        self.assertEqual(currency_display(value, include_sign=True), '$1.23')

    def test_include_sign_false(self):
        value = 123
        self.assertEqual(currency_display(value, include_sign=False), '1.23')
