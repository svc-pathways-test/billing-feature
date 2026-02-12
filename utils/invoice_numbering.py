"""Sequential invoice numbering system."""

class InvoiceNumbering:
    def __init__(self, prefix="INV", start=1000):
        self.prefix = prefix
        self.counter = start

    def next(self):
        self.counter += 1
        return f"{self.prefix}-{self.counter:06d}"

    def parse(self, number):
        parts = number.split("-")
        return {"prefix": parts[0], "sequence": int(parts[1])}
