"""Discount calculation utilities."""

def apply_percentage_discount(amount, percent):
    return amount * (1 - percent / 100)

def apply_flat_discount(amount, discount):
    return max(0, amount - discount)
