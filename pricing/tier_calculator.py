"""Tiered pricing calculator."""

class TierCalculator:
    def __init__(self, tiers=None):
        self.tiers = tiers or []

    def add_tier(self, up_to, price_per_unit):
        self.tiers.append({"up_to": up_to, "price": price_per_unit})
        self.tiers.sort(key=lambda t: t["up_to"])

    def calculate(self, quantity):
        total = 0
        remaining = quantity
        prev = 0
        for tier in self.tiers:
            units = min(remaining, tier["up_to"] - prev)
            total += units * tier["price"]
            remaining -= units
            prev = tier["up_to"]
            if remaining <= 0:
                break
        return round(total, 2)
