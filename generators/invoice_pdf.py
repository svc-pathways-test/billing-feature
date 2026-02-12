"""Invoice PDF generation module."""

class InvoicePDFGenerator:
    def __init__(self, template="default"):
        self.template = template

    def generate(self, invoice_data):
        return {"filename": f"invoice_{invoice_data['id']}.pdf",
                "template": self.template, "data": invoice_data, "format": "PDF", "generated": True}

    def generate_batch(self, invoices):
        return [self.generate(inv) for inv in invoices]
