"""Customer billing portal."""

class CustomerPortal:
    def __init__(self, billing_service):
        self.billing = billing_service

    def get_dashboard(self, customer_id):
        return {"customer_id": customer_id, "invoices": [], "payments": [], "balance": 0.0, "plan": None}

    def download_invoice(self, invoice_id):
        return {"invoice_id": invoice_id, "format": "pdf", "url": f"/invoices/{invoice_id}/download"}

    def update_payment_method(self, customer_id, method_data):
        return {"customer_id": customer_id, "updated": True}
