"""Invoice validation module."""

class InvoiceValidator:
    def validate(self, invoice):
        errors = []
        if not invoice.customer_id:
            errors.append("Customer ID required")
        if invoice.amount <= 0:
            errors.append("Amount must be positive")
        return len(errors) == 0, errors
