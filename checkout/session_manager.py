"""Checkout session manager."""
import secrets
from datetime import datetime, timedelta

class CheckoutSession:
    def __init__(self, ttl_minutes=30):
        self.ttl = ttl_minutes
        self.sessions = {}

    def create(self, customer_id, items, currency="USD"):
        session_id = f"cs_{secrets.token_hex(16)}"
        total = sum(i["price"] * i.get("qty", 1) for i in items)
        self.sessions[session_id] = {"customer_id": customer_id, "items": items, "total": total, "currency": currency, "expires": (datetime.utcnow() + timedelta(minutes=self.ttl)).isoformat(), "status": "open"}
        return session_id, self.sessions[session_id]

    def complete(self, session_id):
        s = self.sessions.get(session_id)
        if s and s["status"] == "open":
            s["status"] = "completed"
            return s
        return None
