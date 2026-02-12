"""Dunning management for failed payments."""

class DunningManager:
    def __init__(self, max_attempts=4):
        self.max_attempts = max_attempts
        self.cases = {}

    def open_case(self, invoice_id, customer_id):
        self.cases[invoice_id] = {"customer_id": customer_id, "attempts": 0, "status": "open"}
        return self.cases[invoice_id]

    def record_attempt(self, invoice_id, success=False):
        case = self.cases.get(invoice_id)
        if not case:
            return None
        case["attempts"] += 1
        if success:
            case["status"] = "resolved"
        elif case["attempts"] >= self.max_attempts:
            case["status"] = "escalated"
        return case

    def get_open_cases(self):
        return {k: v for k, v in self.cases.items() if v["status"] == "open"}
