"""Billing data cache layer."""
from datetime import datetime, timedelta

class BillingCache:
    def __init__(self, ttl_seconds=300):
        self.ttl = ttl_seconds
        self.store = {}

    def get(self, key):
        entry = self.store.get(key)
        if not entry:
            return None
        if datetime.utcnow() > entry["expires"]:
            del self.store[key]
            return None
        return entry["value"]

    def set(self, key, value):
        self.store[key] = {"value": value, "expires": datetime.utcnow() + timedelta(seconds=self.ttl)}

    def invalidate(self, key):
        self.store.pop(key, None)

    def clear(self):
        self.store = {}
