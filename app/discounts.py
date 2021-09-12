"""Module for calculating discounts"""
from typing import Union


def calculate_discounts(user_type: str,
                        amount: Union[int, float],
                        years: Union[int, float],
                        grocery_p: bool) -> Union[int, float]:
    """Calculate discounts according to the following criteria:

If the user is an employee of the store, he gets a 30% discount; If
the user is an affiliate of the store, he gets a 10% discount; If the
user has been a customer for over 2 years, he gets a 5% discount; For
every $100 on the bill, there would be a $5 discount (e.g. for $990,
you get $45 as a discount). The percentage based discounts do not
apply on groceries.  A user can get only one of the percentage based
discounts on a bill

    """
    _rates = {
        "employee": 0.3,
        "affiliate": 0.1,
    }
    proportion_discount = (amount // 100) * 5
    percentage_discount = _rates.get(user_type, 0) * amount
    if years > 2:
        percentage_discount = 0.5 * amount
    if grocery_p:
        percentage_discount = 0
    return amount - (proportion_discount + percentage_discount)
