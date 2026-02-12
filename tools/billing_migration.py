"""Billing data migration tool."""

class BillingMigration:
    def __init__(self):
        self.migrations = []
        self.applied = []

    def add(self, name, up_fn, down_fn):
        self.migrations.append({"name": name, "up": up_fn, "down": down_fn})

    def migrate(self):
        results = []
        for m in self.migrations:
            if m["name"] not in self.applied:
                m["up"]()
                self.applied.append(m["name"])
                results.append({"name": m["name"], "status": "applied"})
        return results

    def rollback(self, steps=1):
        rolled = []
        for _ in range(min(steps, len(self.applied))):
            name = self.applied.pop()
            m = next(m for m in self.migrations if m["name"] == name)
            m["down"]()
            rolled.append(name)
        return rolled
