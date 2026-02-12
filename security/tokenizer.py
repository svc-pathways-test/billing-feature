"""Payment tokenization service."""
import hashlib
import secrets

class PaymentTokenizer:
    def __init__(self):
        self.vault = {}

    def tokenize(self, card_number):
        token = f"tok_{secrets.token_hex(16)}"
        masked = f"****{card_number[-4:]}"
        self.vault[token] = {"masked": masked, "hash": hashlib.sha256(card_number.encode()).hexdigest()}
        return token, masked

    def get_masked(self, token):
        entry = self.vault.get(token)
        return entry["masked"] if entry else None
