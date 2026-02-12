"""Wire transfer payment handler."""

class WireTransferHandler:
    def __init__(self):
        self.pending_transfers = {}

    def initiate(self, invoice_id, amount, bank_details):
        ref = f"WT-{invoice_id}"
        self.pending_transfers[ref] = {"invoice_id": invoice_id, "amount": amount, "bank": bank_details, "status": "pending"}
        return ref, self.pending_transfers[ref]

    def confirm(self, reference, confirmed_amount):
        transfer = self.pending_transfers.get(reference)
        if transfer and abs(transfer["amount"] - confirmed_amount) < 0.01:
            transfer["status"] = "confirmed"
            return transfer
        return None

    def get_pending(self):
        return {k: v for k, v in self.pending_transfers.items() if v["status"] == "pending"}
