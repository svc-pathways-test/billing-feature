"""Plan model definition."""

class Plan:
    def __init__(self, id, name, monthly_price):
        self.id = id
        self.name = name
        self.monthly_price = monthly_price

    @property
    def yearly_price(self):
        return self.monthly_price * 10
