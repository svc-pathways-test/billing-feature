"""Subscription downgrade handler."""

class SubscriptionDowngrade:
    def __init__(self):
        self.pending_downgrades = {}

    def schedule(self, subscription_id, new_plan_id, effective_at="end_of_period"):
        self.pending_downgrades[subscription_id] = {"new_plan": new_plan_id, "effective_at": effective_at, "status": "scheduled"}
        return self.pending_downgrades[subscription_id]

    def execute(self, subscription_id):
        dg = self.pending_downgrades.get(subscription_id)
        if dg and dg["status"] == "scheduled":
            dg["status"] = "executed"
            return dg
        return None

    def cancel(self, subscription_id):
        return self.pending_downgrades.pop(subscription_id, None)
