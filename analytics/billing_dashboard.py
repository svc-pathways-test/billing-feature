"""Billing analytics dashboard."""
from collections import defaultdict

class BillingDashboard:
    def __init__(self, transactions=None):
        self.transactions = transactions or []

    def mrr(self):
        recurring = [t for t in self.transactions if t.get("recurring")]
        return sum(t["amount"] for t in recurring)

    def churn_rate(self, total_customers, lost_customers):
        return round(lost_customers / max(total_customers, 1) * 100, 2)

    def arpu(self, total_revenue, total_customers):
        return round(total_revenue / max(total_customers, 1), 2)

    def ltv(self, arpu, avg_lifetime_months):
        return round(arpu * avg_lifetime_months, 2)
