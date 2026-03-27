"""Payment logging utility."""
import json
from datetime import datetime

class PaymentLogger:
    def log(self, event_type, data):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "event": event_type,
            "data": data
        }
        print(json.dumps(entry))
