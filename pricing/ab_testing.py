"""Pricing A/B testing framework."""
import hashlib

class PricingABTest:
    def __init__(self, test_name, variants):
        self.test_name = test_name
        self.variants = variants
        self.results = {v: {"views": 0, "conversions": 0} for v in variants}

    def assign_variant(self, customer_id):
        h = int(hashlib.md5(f"{self.test_name}:{customer_id}".encode()).hexdigest(), 16)
        idx = h % len(self.variants)
        return self.variants[idx]

    def record_view(self, variant):
        self.results[variant]["views"] += 1

    def record_conversion(self, variant):
        self.results[variant]["conversions"] += 1

    def conversion_rates(self):
        return {v: round(d["conversions"] / max(d["views"], 1) * 100, 2) for v, d in self.results.items()}
