"""Webhook delivery retry logic."""
from datetime import datetime, timedelta

class WebhookRetry:
    def __init__(self, max_retries=5, base_delay=60):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.queue = []

    def schedule_retry(self, webhook_id, attempt):
        if attempt >= self.max_retries:
            return None
        delay = self.base_delay * (2 ** attempt)
        next_at = datetime.utcnow() + timedelta(seconds=delay)
        entry = {"webhook_id": webhook_id, "attempt": attempt + 1, "next_at": next_at.isoformat()}
        self.queue.append(entry)
        return entry

    def get_due(self):
        now = datetime.utcnow().isoformat()
        return [w for w in self.queue if w["next_at"] <= now]
