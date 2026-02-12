"""Payment gateway abstraction layer."""

class PaymentGateway:
    def __init__(self, provider, api_key):
        self.provider = provider
        self.api_key = api_key
        self.connected = False

    def connect(self):
        self.connected = True
        return {"provider": self.provider, "status": "connected"}

    def charge(self, amount, currency, customer_id):
        if not self.connected:
            raise ConnectionError("Gateway not connected")
        return {"provider": self.provider, "amount": amount, "currency": currency, "customer_id": customer_id, "status": "charged"}

    def void(self, transaction_id):
        return {"provider": self.provider, "transaction_id": transaction_id, "status": "voided"}
