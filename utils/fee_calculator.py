"""Payment processing fee calculator."""

class FeeCalculator:
    PROVIDER_FEES = {
        "stripe": {"percentage": 2.9, "fixed": 0.30},
        "paypal": {"percentage": 3.49, "fixed": 0.49},
        "square": {"percentage": 2.6, "fixed": 0.10},
    }

    def calculate(self, amount, provider="stripe"):
        fees = self.PROVIDER_FEES.get(provider, self.PROVIDER_FEES["stripe"])
        fee = round(amount * fees["percentage"] / 100 + fees["fixed"], 2)
        return {"gross": amount, "fee": fee, "net": round(amount - fee, 2), "provider": provider}

    def cheapest_provider(self, amount):
        costs = {p: self.calculate(amount, p)["fee"] for p in self.PROVIDER_FEES}
        best = min(costs, key=costs.get)
        return best, costs[best]
