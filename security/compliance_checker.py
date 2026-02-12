"""PCI compliance checker."""

class ComplianceChecker:
    REQUIRED_CHECKS = [
        "encryption_at_rest", "encryption_in_transit", "access_controls",
        "audit_logging", "vulnerability_scanning", "network_segmentation"
    ]

    def __init__(self):
        self.results = {}

    def run_check(self, check_name, passed=True):
        self.results[check_name] = passed

    def is_compliant(self):
        return all(self.results.get(c, False) for c in self.REQUIRED_CHECKS)

    def report(self):
        return {"compliant": self.is_compliant(), "checks": {c: self.results.get(c, "not_run") for c in self.REQUIRED_CHECKS}}
