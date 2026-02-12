"""Subscription addon management."""

class AddonManager:
    def __init__(self):
        self.addons = {}
        self.subscriptions = {}

    def register_addon(self, addon_id, name, price):
        self.addons[addon_id] = {"name": name, "price": price}

    def attach(self, subscription_id, addon_id):
        if subscription_id not in self.subscriptions:
            self.subscriptions[subscription_id] = []
        self.subscriptions[subscription_id].append(addon_id)

    def total_addon_cost(self, subscription_id):
        addon_ids = self.subscriptions.get(subscription_id, [])
        return sum(self.addons[a]["price"] for a in addon_ids if a in self.addons)
