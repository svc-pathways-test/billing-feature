"""Configurable refund policy engine."""
from datetime import datetime, timedelta

class RefundPolicy:
    def __init__(self, full_refund_days=30, partial_refund_days=60, partial_pct=50):
        self.full_days = full_refund_days
        self.partial_days = partial_refund_days
        self.partial_pct = partial_pct

    def evaluate(self, purchase_date, amount):
        if isinstance(purchase_date, str):
            purchase_date = datetime.fromisoformat(purchase_date)
        days = (datetime.utcnow() - purchase_date).days
        if days <= self.full_days:
            return {"eligible": True, "amount": amount, "type": "full"}
        elif days <= self.partial_days:
            return {"eligible": True, "amount": round(amount * self.partial_pct / 100, 2), "type": "partial"}
        return {"eligible": False, "amount": 0, "type": "none"}
