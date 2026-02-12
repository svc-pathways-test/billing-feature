"""Payment method storage and management."""
from collections import defaultdict

class PaymentMethodStore:
    def __init__(self):
        self.methods = defaultdict(list)

    def add(self, customer_id, method_type, token, is_default=False):
        method = {"type": method_type, "token": token, "default": is_default}
        self.methods[customer_id].append(method)
        return method

    def get_default(self, customer_id):
        for m in self.methods[customer_id]:
            if m["default"]:
                return m
        return self.methods[customer_id][0] if self.methods[customer_id] else None
