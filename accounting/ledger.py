"""Double-entry accounting ledger."""

class Ledger:
    def __init__(self):
        self.entries = []

    def record(self, debit_account, credit_account, amount, description=""):
        entry = {"debit": debit_account, "credit": credit_account, "amount": amount, "desc": description}
        self.entries.append(entry)
        return entry

    def balance(self, account):
        debits = sum(e["amount"] for e in self.entries if e["debit"] == account)
        credits = sum(e["amount"] for e in self.entries if e["credit"] == account)
        return debits - credits
