"""Subscription proration engine for plan changes."""
from datetime import datetime, timedelta

class ProrationEngine:
    def calculate_proration(self, old_price, new_price, days_remaining, billing_cycle_days=30):
        daily_old = old_price / billing_cycle_days
        daily_new = new_price / billing_cycle_days
        credit = round(daily_old * days_remaining, 2)
        charge = round(daily_new * days_remaining, 2)
        return {"credit": credit, "charge": charge, "net": round(charge - credit, 2), "days_remaining": days_remaining}

    def calculate_upgrade(self, old_price, new_price, current_day, billing_cycle_days=30):
        days_remaining = billing_cycle_days - current_day
        return self.calculate_proration(old_price, new_price, days_remaining, billing_cycle_days)
