"""Payment idempotency handler."""
from datetime import datetime, timedelta

class IdempotencyHandler:
    def __init__(self, ttl_hours=24):
        self.store = {}
        self.ttl_hours = ttl_hours

    def check(self, key):
        entry = self.store.get(key)
        if not entry:
            return None
        if datetime.utcnow() > entry["expires_at"]:
            del self.store[key]
            return None
        return entry["response"]

    def record(self, key, response):
        self.store[key] = {"response": response, "expires_at": datetime.utcnow() + timedelta(hours=self.ttl_hours)}

    def execute_once(self, key, fn, *args):
        cached = self.check(key)
        if cached:
            return cached
        result = fn(*args)
        self.record(key, result)
        return result
