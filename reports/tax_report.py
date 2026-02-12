"""Tax reporting module."""
from collections import defaultdict

class TaxReport:
    def __init__(self, transactions=None):
        self.transactions = transactions or []

    def by_region(self):
        grouped = defaultdict(float)
        for t in self.transactions:
            grouped[t.get("region", "unknown")] += t.get("tax", 0)
        return dict(grouped)

    def total_collected(self, start=None, end=None):
        filtered = [t for t in self.transactions if (not start or t.get("date","") >= start) and (not end or t.get("date","") <= end)]
        return round(sum(t.get("tax", 0) for t in filtered), 2)

    def summary(self):
        return {"total_tax": self.total_collected(), "by_region": self.by_region(), "transaction_count": len(self.transactions)}
