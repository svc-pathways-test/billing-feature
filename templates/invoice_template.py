"""Invoice template engine."""

class InvoiceTemplate:
    def __init__(self, name, header="", footer=""):
        self.name = name
        self.header = header
        self.footer = footer

    def render(self, invoice_data):
        lines = [self.header, f"Invoice #{invoice_data["id"]}", f"Amount: {invoice_data["amount"]}"]
        for item in invoice_data.get("items", []):
            lines.append(f"  - {item["name"]}: {item["price"]}")
        lines.append(self.footer)
        return "\n".join(lines)
