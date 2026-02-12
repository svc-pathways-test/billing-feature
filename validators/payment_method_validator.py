"""Payment method validation."""

class PaymentMethodValidator:
    def validate_card(self, number):
        digits = [int(d) for d in number if d.isdigit()]
        if len(digits) < 13 or len(digits) > 19:
            return False, "Invalid card length"
        checksum = 0
        for i, d in enumerate(reversed(digits)):
            if i % 2 == 1:
                d *= 2
                if d > 9:
                    d -= 9
            checksum += d
        return checksum % 10 == 0, "Valid" if checksum % 10 == 0 else "Invalid checksum"

    def detect_brand(self, number):
        if number.startswith("4"):
            return "visa"
        elif number[:2] in ("51","52","53","54","55"):
            return "mastercard"
        elif number[:2] in ("34","37"):
            return "amex"
        return "unknown"
