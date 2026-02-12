"""Payment escrow service."""

class EscrowService:
    def __init__(self):
        self.escrows = {}

    def hold(self, transaction_id, amount, payer_id, payee_id):
        self.escrows[transaction_id] = {"amount": amount, "payer": payer_id, "payee": payee_id, "status": "held"}
        return self.escrows[transaction_id]

    def release(self, transaction_id):
        e = self.escrows.get(transaction_id)
        if e and e["status"] == "held":
            e["status"] = "released"
            return e
        return None

    def refund(self, transaction_id):
        e = self.escrows.get(transaction_id)
        if e and e["status"] == "held":
            e["status"] = "refunded"
            return e
        return None
