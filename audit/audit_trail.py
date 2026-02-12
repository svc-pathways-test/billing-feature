"""Billing audit trail for compliance tracking."""
from datetime import datetime

class AuditTrail:
    def __init__(self):
        self.entries = []

    def record(self, action, entity_type, entity_id, details=None):
        entry = {"timestamp": datetime.utcnow().isoformat(), "action": action,
                 "entity_type": entity_type, "entity_id": entity_id, "details": details or {}}
        self.entries.append(entry)
        return entry

    def get_history(self, entity_id):
        return [e for e in self.entries if e["entity_id"] == entity_id]
