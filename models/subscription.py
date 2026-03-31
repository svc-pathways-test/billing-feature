"""Subscription model definition."""

class Subscription:
    def __init__(self, id, plan_id, customer_id):
        self.id = id
        self.plan_id = plan_id
        self.customer_id = customer_id
        self.active = True

    def cancel(self):
        self.active = False
