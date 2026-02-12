"""Payment reconciliation service."""

class PaymentReconciler:
    def reconcile(self, invoices, payments):
        inv_map = {i["id"]: i for i in invoices}
        matched, unmatched_payments, unpaid = [], [], []
        for p in payments:
            if p.get("invoice_id") in inv_map:
                matched.append({"invoice": inv_map.pop(p["invoice_id"]), "payment": p})
            else:
                unmatched_payments.append(p)
        unpaid = list(inv_map.values())
        return {"matched": matched, "unmatched_payments": unmatched_payments, "unpaid_invoices": unpaid}
