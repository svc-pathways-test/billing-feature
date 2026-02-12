"""Payment analytics tracker."""
from collections import defaultdict

class PaymentAnalytics:
    def __init__(self):
        self.events = []

    def track(self, event_type, amount, provider, success=True):
        self.events.append({"type": event_type, "amount": amount, "provider": provider, "success": success})

    def success_rate(self, provider=None):
        filtered = [e for e in self.events if not provider or e["provider"] == provider]
        if not filtered:
            return 0
        return round(sum(1 for e in filtered if e["success"]) / len(filtered) * 100, 2)

    def total_volume(self):
        return round(sum(e["amount"] for e in self.events if e["success"]), 2)
