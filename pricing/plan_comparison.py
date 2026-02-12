"""Plan comparison tool."""

class PlanComparison:
    def __init__(self):
        self.plans = {}

    def add_plan(self, plan_id, name, price, features):
        self.plans[plan_id] = {"name": name, "price": price, "features": set(features)}

    def compare(self, plan_a, plan_b):
        a, b = self.plans[plan_a], self.plans[plan_b]
        return {
            "only_in_a": list(a["features"] - b["features"]),
            "only_in_b": list(b["features"] - a["features"]),
            "common": list(a["features"] & b["features"]),
            "price_diff": b["price"] - a["price"]
        }

    def recommend(self, required_features):
        required = set(required_features)
        eligible = [(pid, p) for pid, p in self.plans.items() if required <= p["features"]]
        eligible.sort(key=lambda x: x[1]["price"])
        return eligible[0][0] if eligible else None
