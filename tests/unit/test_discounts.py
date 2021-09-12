"""Test cases for app/discounts.py"""
from unittest import TestCase

from app.discounts import calculate_discounts


class TestDiscounts(TestCase):
    """Test cases for calculating discounts"""

    def test_employee_discount(self):
        """Test that employee discount is calculated correctly"""
        self.assertEqual(
            calculate_discounts(user_type="employee",
                                amount=990,
                                years=1,
                                grocery_p=False),
            648)

    def test_affiliate_discount(self):
        """Test that affiliate discount is calculated correctly"""
        self.assertEqual(
            calculate_discounts(user_type="affiliate",
                                amount=990,
                                years=1,
                                grocery_p=False),
            846)

    def test_three_year_long_discount(self):
        """Test that amount type with years > 3 is calculated correctly"""
        self.assertEqual(
            calculate_discounts(user_type="employee",
                                amount=990,
                                years=3,
                                grocery_p=False),
            450)

    def test_three_year_long_employee_discount_with_groceries(self):
        """Test that amount with groceries is calculated correctly"""
        self.assertEqual(
            calculate_discounts(user_type="affiliate",
                                amount=990,
                                years=3,
                                grocery_p=True),
            945)
