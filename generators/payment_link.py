"""Payment link generator."""
import secrets

class PaymentLinkGenerator:
    def __init__(self, base_url="https://pay.example.com"):
        self.base_url = base_url
        self.links = {}

    def create(self, amount, currency="USD", description="", expires_hours=72):
        token = secrets.token_urlsafe(32)
        link = {"url": f"{self.base_url}/{token}", "amount": amount, "currency": currency, "description": description, "active": True}
        self.links[token] = link
        return link

    def deactivate(self, token):
        if token in self.links:
            self.links[token]["active"] = False
            return True
        return False
