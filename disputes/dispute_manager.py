"""Payment dispute management."""

class DisputeManager:
    def __init__(self):
        self.disputes = {}

    def open_dispute(self, transaction_id, reason, amount):
        self.disputes[transaction_id] = {"reason": reason, "amount": amount, "status": "open"}
        return self.disputes[transaction_id]

    def resolve(self, transaction_id, outcome):
        if transaction_id in self.disputes:
            self.disputes[transaction_id]["status"] = outcome
            return self.disputes[transaction_id]
        return None

    def get_open(self):
        return {k: v for k, v in self.disputes.items() if v["status"] == "open"}
