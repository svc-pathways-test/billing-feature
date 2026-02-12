"""Recurring invoice scheduler."""
from datetime import datetime, timedelta

class InvoiceScheduler:
    def __init__(self):
        self.schedules = []

    def add_schedule(self, customer_id, amount, interval="monthly"):
        schedule = {"customer_id": customer_id, "amount": amount, "interval": interval, "next_run": self._next_date(interval), "active": True}
        self.schedules.append(schedule)
        return schedule

    def _next_date(self, interval):
        now = datetime.utcnow()
        deltas = {"daily": timedelta(days=1), "weekly": timedelta(weeks=1), "monthly": timedelta(days=30)}
        return (now + deltas.get(interval, timedelta(days=30))).isoformat()

    def get_due(self):
        now = datetime.utcnow().isoformat()
        return [s for s in self.schedules if s["active"] and s["next_run"] <= now]
