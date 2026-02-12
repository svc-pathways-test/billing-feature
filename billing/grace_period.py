"""Payment grace period handler."""
from datetime import datetime, timedelta

class GracePeriod:
    def __init__(self, days=7):
        self.days = days

    def is_within_grace(self, due_date):
        if isinstance(due_date, str):
            due_date = datetime.fromisoformat(due_date)
        deadline = due_date + timedelta(days=self.days)
        return datetime.utcnow() <= deadline

    def days_remaining(self, due_date):
        if isinstance(due_date, str):
            due_date = datetime.fromisoformat(due_date)
        deadline = due_date + timedelta(days=self.days)
        remaining = (deadline - datetime.utcnow()).days
        return max(0, remaining)
