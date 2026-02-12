"""Coupon management system."""
from datetime import datetime

class CouponManager:
    def __init__(self):
        self.coupons = {}

    def create(self, code, discount_type, value, expires_at=None):
        self.coupons[code] = {"type": discount_type, "value": value, "expires_at": expires_at, "used": 0}
        return self.coupons[code]

    def validate(self, code):
        coupon = self.coupons.get(code)
        if not coupon:
            return False, "Invalid coupon code"
        if coupon["expires_at"] and datetime.utcnow().isoformat() > coupon["expires_at"]:
            return False, "Coupon expired"
        return True, coupon

    def apply(self, code, amount):
        valid, result = self.validate(code)
        if not valid:
            return amount, result
        if result["type"] == "percentage":
            return round(amount * (1 - result["value"] / 100), 2), "Applied"
        return round(max(0, amount - result["value"]), 2), "Applied"
