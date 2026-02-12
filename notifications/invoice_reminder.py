"""Invoice reminder scheduler."""
from datetime import datetime, timedelta

class InvoiceReminder:
    def __init__(self, remind_days_before=None):
        self.remind_days = remind_days_before or [7, 3, 1]
        self.sent = {}

    def check_due(self, invoice_id, due_date):
        if isinstance(due_date, str):
            due_date = datetime.fromisoformat(due_date)
        days_until = (due_date - datetime.utcnow()).days
        for d in self.remind_days:
            if days_until <= d and (invoice_id, d) not in self.sent:
                self.sent[(invoice_id, d)] = True
                return {"send": True, "days_until_due": days_until, "reminder_level": d}
        return {"send": False}
