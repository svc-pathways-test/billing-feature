"""Multi-currency pricing engine."""

class MultiCurrencyEngine:
    def __init__(self):
        self.rates = {"USD": 1.0, "EUR": 0.92, "GBP": 0.79, "JPY": 149.50, "CAD": 1.36, "AUD": 1.53}

    def set_rate(self, currency, rate):
        self.rates[currency] = rate

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError(f"Unsupported currency pair: {from_currency}/{to_currency}")
        usd_amount = amount / self.rates[from_currency]
        return round(usd_amount * self.rates[to_currency], 2)

    def get_price_table(self, base_amount, base_currency="USD"):
        return {curr: self.convert(base_amount, base_currency, curr) for curr in self.rates}
