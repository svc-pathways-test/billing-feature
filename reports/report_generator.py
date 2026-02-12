"""Billing reports generator."""
from collections import defaultdict

class ReportGenerator:
    def __init__(self, transactions=None):
        self.transactions = transactions or []

    def revenue_summary(self, start_date=None, end_date=None):
        filtered = self._filter_by_date(start_date, end_date)
        total = sum(t["amount"] for t in filtered if t["type"] == "payment")
        refunds = sum(t["amount"] for t in filtered if t["type"] == "refund")
        return {"gross_revenue": total, "refunds": refunds, "net_revenue": total - refunds, "count": len(filtered)}

    def by_customer(self):
        grouped = defaultdict(float)
        for t in self.transactions:
            grouped[t["customer_id"]] += t["amount"]
        return dict(grouped)

    def _filter_by_date(self, start, end):
        return [t for t in self.transactions if (not start or t.get("date", "") >= start) and (not end or t.get("date", "") <= end)]
