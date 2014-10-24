from random import random

class Weapon:

    def __init__(self, type, damage, critical_strike_percent):
        self.type = type
        self.damage = damage
        self._set_critical_strike_percent(critical_strike_percent)

    def _set_critical_strike_percent(self, critical_strike_percent):
        if critical_strike_percent > 0 and critical_strike_percent < 1:
            self.critical_strike_percent = critical_strike_percent

        else:
            raise ValueError

    def critical_hit(self):
        chance = random()
        if chance < self.critical_strike_percent:
            return True
        return False
