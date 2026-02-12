"""Invoice aging report."""
from datetime import datetime

class InvoiceAging:
    BUCKETS = [(0, 30, "current"), (31, 60, "30_days"), (61, 90, "60_days"), (91, float("inf"), "90_plus")]

    def categorize(self, invoices):
        report = {b[2]: [] for b in self.BUCKETS}
        for inv in invoices:
            if inv.get("paid"):
                continue
            due = datetime.fromisoformat(inv["due_date"]) if isinstance(inv["due_date"], str) else inv["due_date"]
            days = (datetime.utcnow() - due).days
            for low, high, label in self.BUCKETS:
                if low <= days <= high:
                    report[label].append(inv)
                    break
        return report

    def totals(self, invoices):
        report = self.categorize(invoices)
        return {k: sum(i["amount"] for i in v) for k, v in report.items()}
