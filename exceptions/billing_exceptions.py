"""Custom billing exceptions."""

class BillingError(Exception):
    pass

class PaymentFailedError(BillingError):
    pass

class InvalidInvoiceError(BillingError):
    pass

class RefundNotAllowedError(BillingError):
    pass
