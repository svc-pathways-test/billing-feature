"""Payment splitting for marketplace transactions."""

class PaymentSplitter:
    def split(self, total, splits):
        results = []
        for s in splits:
            amt = round(total * s["percentage"] / 100, 2)
            results.append({"recipient": s["recipient"], "amount": amt})
        return results

    def validate_splits(self, splits):
        total_pct = sum(s["percentage"] for s in splits)
        return abs(total_pct - 100) < 0.01
