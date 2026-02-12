"""Billing event bus for decoupled communication."""
from collections import defaultdict

class EventBus:
    def __init__(self):
        self.subscribers = defaultdict(list)
        self.history = []

    def subscribe(self, event_type, handler):
        self.subscribers[event_type].append(handler)

    def publish(self, event_type, data):
        event = {"type": event_type, "data": data}
        self.history.append(event)
        for handler in self.subscribers.get(event_type, []):
            handler(event)
        return len(self.subscribers.get(event_type, []))

    def replay(self, event_type=None):
        events = self.history if not event_type else [e for e in self.history if e["type"] == event_type]
        return events
