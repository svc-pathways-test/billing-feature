"""Billing API endpoints."""

class BillingAPI:
    def __init__(self, config):
        self.config = config

    def create_invoice(self, data):
        return {"id": "inv_123", **data}

    def get_invoice(self, invoice_id):
        return {"id": invoice_id, "status": "pending"}
