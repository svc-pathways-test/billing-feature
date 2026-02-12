"""Metered billing calculator."""
from collections import defaultdict

class MeteredBilling:
    def __init__(self, rate_per_unit=0.01):
        self.rate = rate_per_unit
        self.usage = defaultdict(int)

    def record_usage(self, customer_id, units):
        self.usage[customer_id] += units
        return self.usage[customer_id]

    def calculate_charge(self, customer_id):
        units = self.usage[customer_id]
        return {"customer_id": customer_id, "units": units, "charge": round(units * self.rate, 2)}

    def reset(self, customer_id):
        total = self.usage[customer_id]
        self.usage[customer_id] = 0
        return total
