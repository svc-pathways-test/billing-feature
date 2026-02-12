"""Async payment processing queue."""
from collections import deque

class PaymentQueue:
    def __init__(self, max_size=1000):
        self.queue = deque(maxlen=max_size)
        self.processed = []

    def enqueue(self, payment):
        self.queue.append(payment)
        return len(self.queue)

    def process_next(self, processor_fn):
        if not self.queue:
            return None
        payment = self.queue.popleft()
        result = processor_fn(payment)
        self.processed.append({"payment": payment, "result": result})
        return result

    def pending_count(self):
        return len(self.queue)
