"""Billing utility functions."""

def calculate_tax(amount, rate=0.08):
    return round(amount * rate, 2)

def format_currency(amount, currency="USD"):
    return f"{currency} {amount:.2f}"
