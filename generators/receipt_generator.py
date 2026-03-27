"""Receipt generation module."""

class ReceiptGenerator:
    def __init__(self, invoice):
        self.invoice = invoice

    def generate(self):
        return {
            "invoice_id": self.invoice.id,
            "amount": self.invoice.amount,
            "status": "paid"
        }
