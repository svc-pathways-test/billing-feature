"""Billing configuration module."""
import os

class BillingConfig:
    def __init__(self):
        self.stripe_key = os.getenv("STRIPE_KEY", "")
        self.tax_enabled = True
        self.default_currency = "USD"

    def is_valid(self):
        return bool(self.stripe_key)
