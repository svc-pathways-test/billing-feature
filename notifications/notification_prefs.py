"""Billing notification preferences."""

class NotificationPreferences:
    def __init__(self):
        self.prefs = {}

    def set_preferences(self, customer_id, channels=None, frequency="immediate"):
        self.prefs[customer_id] = {"channels": channels or ["email"], "frequency": frequency, "enabled": True}
        return self.prefs[customer_id]

    def get_preferences(self, customer_id):
        return self.prefs.get(customer_id, {"channels": ["email"], "frequency": "immediate", "enabled": True})

    def should_notify(self, customer_id, channel):
        p = self.get_preferences(customer_id)
        return p["enabled"] and channel in p["channels"]

    def disable(self, customer_id):
        if customer_id in self.prefs:
            self.prefs[customer_id]["enabled"] = False
