"""Fraud detection engine for billing."""

class FraudDetector:
    def __init__(self, threshold=0.7):
        self.threshold = threshold
        self.rules = []

    def add_rule(self, name, check_fn):
        self.rules.append({"name": name, "check": check_fn})

    def evaluate(self, transaction):
        score = sum(1 for r in self.rules if r["check"](transaction)) / max(len(self.rules), 1)
        return {"score": score, "flagged": score >= self.threshold}
