"""Currency conversion utility."""

RATES = {"USD": 1.0, "EUR": 0.85, "GBP": 0.73}

def convert(amount, from_curr, to_curr):
    if from_curr == to_curr:
        return amount
    usd = amount / RATES[from_curr]
    return round(usd * RATES[to_curr], 2)
