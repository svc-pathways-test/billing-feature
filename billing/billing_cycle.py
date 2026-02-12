"""Billing cycle management."""
from datetime import datetime, timedelta

class BillingCycle:
    def __init__(self, anchor_day=1):
        self.anchor_day = anchor_day

    def current_period(self, ref_date=None):
        ref = ref_date or datetime.utcnow()
        start = ref.replace(day=self.anchor_day)
        if ref.day < self.anchor_day:
            start = (start - timedelta(days=32)).replace(day=self.anchor_day)
        end = (start + timedelta(days=32)).replace(day=self.anchor_day) - timedelta(days=1)
        return {"start": start.isoformat(), "end": end.isoformat()}
