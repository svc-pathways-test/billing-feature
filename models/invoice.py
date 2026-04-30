"""Invoice model definition."""

class Invoice:
    def __init__(self, id, amount, customer_id):
        self.id = id
        self.amount = amount
        self.customer_id = customer_id

    def validate(self):
        return self.amount > 0
