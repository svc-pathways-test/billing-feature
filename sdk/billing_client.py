"""Billing API client SDK."""

class BillingClient:
    def __init__(self, api_key, base_url="https://api.billing.example.com"):
        self.api_key = api_key
        self.base_url = base_url

    def _headers(self):
        return {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}

    def create_invoice(self, customer_id, items):
        return {"endpoint": f"{self.base_url}/invoices", "method": "POST", "body": {"customer_id": customer_id, "items": items}}

    def get_invoice(self, invoice_id):
        return {"endpoint": f"{self.base_url}/invoices/{invoice_id}", "method": "GET"}

    def create_payment(self, invoice_id, amount):
        return {"endpoint": f"{self.base_url}/payments", "method": "POST", "body": {"invoice_id": invoice_id, "amount": amount}}
