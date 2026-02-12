"""Webhook signature verification."""
import hashlib
import hmac

class WebhookSignatureVerifier:
    def __init__(self, secret):
        self.secret = secret.encode("utf-8")

    def sign(self, payload):
        return hmac.new(self.secret, payload.encode("utf-8"), hashlib.sha256).hexdigest()

    def verify(self, payload, signature):
        expected = self.sign(payload)
        return hmac.compare_digest(expected, signature)

    def sign_with_timestamp(self, payload, timestamp):
        message = f"{timestamp}.{payload}"
        return self.sign(message)

    def verify_with_timestamp(self, payload, timestamp, signature, max_age_seconds=300):
        import time
        if abs(time.time() - timestamp) > max_age_seconds:
            return False, "Timestamp too old"
        return self.verify(f"{timestamp}.{payload}", signature), "Valid"
