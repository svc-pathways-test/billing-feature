"""Chargeback handling workflow."""

class ChargebackHandler:
    def __init__(self):
        self.chargebacks = {}

    def receive(self, transaction_id, amount, reason_code):
        self.chargebacks[transaction_id] = {"amount": amount, "reason": reason_code, "status": "received", "evidence": None}
        return self.chargebacks[transaction_id]

    def submit_evidence(self, transaction_id, evidence):
        cb = self.chargebacks.get(transaction_id)
        if cb:
            cb["evidence"] = evidence
            cb["status"] = "disputed"
        return cb

    def resolve(self, transaction_id, won=True):
        cb = self.chargebacks.get(transaction_id)
        if cb:
            cb["status"] = "won" if won else "lost"
        return cb
