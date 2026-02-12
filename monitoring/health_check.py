"""Billing system health checker."""
from datetime import datetime

class BillingHealthCheck:
    def __init__(self):
        self.checks = {}

    def register(self, name, check_fn):
        self.checks[name] = check_fn

    def run_all(self):
        results = {}
        for name, fn in self.checks.items():
            try:
                fn()
                results[name] = {"status": "healthy", "checked_at": datetime.utcnow().isoformat()}
            except Exception as e:
                results[name] = {"status": "unhealthy", "error": str(e), "checked_at": datetime.utcnow().isoformat()}
        all_healthy = all(r["status"] == "healthy" for r in results.values())
        return {"overall": "healthy" if all_healthy else "degraded", "checks": results}
