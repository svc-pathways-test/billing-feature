"""Payment retry mechanism with exponential backoff."""
import time

class PaymentRetry:
    def __init__(self, max_retries=3, base_delay=1.0):
        self.max_retries = max_retries
        self.base_delay = base_delay

    def execute_with_retry(self, payment_fn, *args):
        last_error = None
        for attempt in range(self.max_retries):
            try:
                result = payment_fn(*args)
                return {"status": "success", "attempt": attempt + 1, "result": result}
            except Exception as e:
                last_error = e
                delay = self.base_delay * (2 ** attempt)
                time.sleep(delay)
        return {"status": "failed", "attempts": self.max_retries, "error": str(last_error)}
