"""Refund processing module."""

class RefundProcessor:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor

    def process_refund(self, transaction_id, amount):
        return {
            "status": "refunded",
            "transaction_id": transaction_id,
            "amount": amount
        }
