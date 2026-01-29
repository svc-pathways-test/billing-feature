"""Stripe payment processor implementation."""

class StripeProcessor:
    def __init__(self, api_key):
        self.api_key = api_key

    def process(self, amount):
        return {"status": "success", "amount": amount}

    def refund(self, transaction_id):
        return {"status": "refunded", "id": transaction_id}
