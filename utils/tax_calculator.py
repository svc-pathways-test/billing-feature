"""Tax calculation engine with region support."""

TAX_RATES = {
    "US-CA": 0.0725, "US-NY": 0.08, "US-TX": 0.0625,
    "EU-DE": 0.19, "EU-FR": 0.20, "GB": 0.20,
}

def calculate_tax(amount, region):
    rate = TAX_RATES.get(region, 0.0)
    return round(amount * rate, 2)

def get_total_with_tax(amount, region):
    tax = calculate_tax(amount, region)
    return round(amount + tax, 2)
