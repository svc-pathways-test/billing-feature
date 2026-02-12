"""Tax exemption handling."""

class TaxExemptionHandler:
    def __init__(self):
        self.exemptions = {}

    def register(self, customer_id, certificate_id, region):
        self.exemptions[customer_id] = {"certificate": certificate_id, "region": region, "verified": False}

    def verify(self, customer_id):
        if customer_id in self.exemptions:
            self.exemptions[customer_id]["verified"] = True
            return True
        return False

    def is_exempt(self, customer_id, region):
        ex = self.exemptions.get(customer_id)
        return ex and ex["verified"] and ex["region"] == region
