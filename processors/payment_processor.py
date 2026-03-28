"""Payment processor interface."""
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount):
        pass

    @abstractmethod
    def refund(self, transaction_id):
        pass
