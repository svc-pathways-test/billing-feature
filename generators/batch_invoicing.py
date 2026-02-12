"""Batch invoice generation."""

class BatchInvoicer:
    def __init__(self, template="default"):
        self.template = template
        self.batch = []

    def add(self, customer_id, items, due_days=30):
        total = sum(i["price"] * i.get("qty", 1) for i in items)
        self.batch.append({"customer_id": customer_id, "items": items, "total": total, "due_days": due_days})

    def generate_all(self):
        return [{"invoice_id": f"INV-{i+1:04d}", **inv} for i, inv in enumerate(self.batch)]

    def clear(self):
        self.batch = []
