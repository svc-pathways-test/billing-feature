"""API quota management for billing plans."""
from collections import defaultdict

class QuotaManager:
    def __init__(self):
        self.limits = {}
        self.usage = defaultdict(lambda: defaultdict(int))

    def set_limit(self, plan_id, resource, limit):
        if plan_id not in self.limits:
            self.limits[plan_id] = {}
        self.limits[plan_id][resource] = limit

    def consume(self, customer_id, plan_id, resource, amount=1):
        limit = self.limits.get(plan_id, {}).get(resource, float("inf"))
        current = self.usage[customer_id][resource]
        if current + amount > limit:
            return False, {"remaining": limit - current}
        self.usage[customer_id][resource] += amount
        return True, {"used": self.usage[customer_id][resource], "limit": limit}
