"""Customer credit balance manager."""
from collections import defaultdict

class CreditManager:
    def __init__(self):
        self.balances = defaultdict(float)
        self.history = defaultdict(list)

    def add_credit(self, customer_id, amount, reason="manual"):
        self.balances[customer_id] += amount
        self.history[customer_id].append({"type": "credit", "amount": amount, "reason": reason})
        return self.balances[customer_id]

    def deduct(self, customer_id, amount):
        if self.balances[customer_id] < amount:
            return None, "Insufficient credits"
        self.balances[customer_id] -= amount
        self.history[customer_id].append({"type": "debit", "amount": amount})
        return self.balances[customer_id], "Success"

    def get_balance(self, customer_id):
        return self.balances[customer_id]
