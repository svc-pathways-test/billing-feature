"""Subscription pause and resume handler."""
from datetime import datetime

class SubscriptionPause:
    def __init__(self):
        self.paused = {}

    def pause(self, subscription_id, reason="user_request"):
        self.paused[subscription_id] = {"paused_at": datetime.utcnow().isoformat(), "reason": reason}
        return self.paused[subscription_id]

    def resume(self, subscription_id):
        if subscription_id in self.paused:
            info = self.paused.pop(subscription_id)
            info["resumed_at"] = datetime.utcnow().isoformat()
            return info
        return None

    def is_paused(self, subscription_id):
        return subscription_id in self.paused
