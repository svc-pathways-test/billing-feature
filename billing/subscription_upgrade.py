"""Subscription upgrade flow."""

class SubscriptionUpgrade:
    def __init__(self, plans=None):
        self.plans = plans or {}

    def register_plan(self, plan_id, name, price, tier):
        self.plans[plan_id] = {"name": name, "price": price, "tier": tier}

    def can_upgrade(self, from_plan, to_plan):
        f = self.plans.get(from_plan)
        t = self.plans.get(to_plan)
        return f and t and t["tier"] > f["tier"]

    def calculate_cost(self, from_plan, to_plan, days_remaining, cycle_days=30):
        diff = self.plans[to_plan]["price"] - self.plans[from_plan]["price"]
        prorated = round(diff * days_remaining / cycle_days, 2)
        return {"price_difference": diff, "prorated_charge": prorated, "days_remaining": days_remaining}
