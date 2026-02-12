"""Billing email notification service."""

class EmailNotifier:
    def __init__(self, smtp_host="localhost", smtp_port=587):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port

    def send_invoice(self, customer_email, invoice_data):
        return {"to": customer_email, "template": "invoice", "data": invoice_data, "sent": True}

    def send_payment_confirmation(self, customer_email, payment_data):
        return {"to": customer_email, "template": "payment_confirmation", "data": payment_data, "sent": True}

    def send_refund_notice(self, customer_email, refund_data):
        return {"to": customer_email, "template": "refund_notice", "data": refund_data, "sent": True}
