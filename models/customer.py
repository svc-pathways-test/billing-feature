"""Customer model definition."""

class Customer:
    def __init__(self, id, email, name):
        self.id = id
        self.email = email
        self.name = name
        self.billing_address = None

    def set_address(self, address):
        self.billing_address = address
