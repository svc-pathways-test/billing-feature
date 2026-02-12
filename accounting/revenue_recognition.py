"""Revenue recognition engine."""
from datetime import datetime

class RevenueRecognition:
    def __init__(self):
        self.entries = []

    def recognize(self, invoice_id, amount, periods):
        per_period = round(amount / periods, 2)
        for i in range(periods):
            self.entries.append({"invoice_id": invoice_id, "period": i + 1, "amount": per_period, "recognized": False})

    def mark_recognized(self, invoice_id, period):
        for e in self.entries:
            if e["invoice_id"] == invoice_id and e["period"] == period:
                e["recognized"] = True
                return e
        return None
