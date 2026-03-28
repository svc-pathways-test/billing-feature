"""Webhook handler for payment events."""

class WebhookHandler:
    def __init__(self):
        self.handlers = {}

    def register(self, event_type, handler):
        self.handlers[event_type] = handler

    def process(self, event):
        handler = self.handlers.get(event["type"])
        return handler(event) if handler else None
