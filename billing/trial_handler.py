"""Subscription trial period handler."""
from datetime import datetime, timedelta

class TrialHandler:
    def __init__(self, default_days=14):
        self.default_days = default_days
        self.trials = {}

    def start_trial(self, customer_id, days=None):
        duration = days or self.default_days
        self.trials[customer_id] = {"start": datetime.utcnow(), "end": datetime.utcnow() + timedelta(days=duration)}
        return self.trials[customer_id]

    def is_active(self, customer_id):
        trial = self.trials.get(customer_id)
        return trial and datetime.utcnow() < trial["end"]

    def days_remaining(self, customer_id):
        trial = self.trials.get(customer_id)
        if not trial:
            return 0
        remaining = (trial["end"] - datetime.utcnow()).days
        return max(0, remaining)
