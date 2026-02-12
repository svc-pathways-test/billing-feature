"""Usage-based billing tracker."""
from collections import defaultdict
from datetime import datetime

class UsageTracker:
    def __init__(self):
        self.usage = defaultdict(list)

    def record(self, customer_id, metric, quantity=1):
        event = {"timestamp": datetime.utcnow().isoformat(), "metric": metric, "quantity": quantity}
        self.usage[customer_id].append(event)
        return event

    def get_total(self, customer_id, metric):
        events = self.usage.get(customer_id, [])
        return sum(e["quantity"] for e in events if e["metric"] == metric)

    def get_summary(self, customer_id):
        events = self.usage.get(customer_id, [])
        summary = defaultdict(int)
        for e in events:
            summary[e["metric"]] += e["quantity"]
        return dict(summary)
