"""Vendor payout management."""

class PayoutManager:
    def __init__(self):
        self.payouts = []
        self.pending = []

    def schedule(self, vendor_id, amount, currency="USD"):
        payout = {"vendor_id": vendor_id, "amount": amount, "currency": currency, "status": "pending"}
        self.pending.append(payout)
        return payout

    def execute_pending(self):
        executed = []
        for p in self.pending:
            p["status"] = "executed"
            executed.append(p)
        self.payouts.extend(executed)
        self.pending = []
        return executed
