"""Feature entitlement engine."""

class EntitlementEngine:
    def __init__(self):
        self.plan_entitlements = {}
        self.overrides = {}

    def define_plan(self, plan_id, features):
        self.plan_entitlements[plan_id] = set(features)

    def override(self, customer_id, feature, enabled=True):
        if customer_id not in self.overrides:
            self.overrides[customer_id] = {}
        self.overrides[customer_id][feature] = enabled

    def has_access(self, customer_id, plan_id, feature):
        if customer_id in self.overrides and feature in self.overrides[customer_id]:
            return self.overrides[customer_id][feature]
        return feature in self.plan_entitlements.get(plan_id, set())
