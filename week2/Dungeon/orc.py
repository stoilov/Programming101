from entity import Entity


class Orc(Entity):

    def __init__(self, name, health, berserk):
        super().__init__(name, health)
        self.berserk_check(berserk)
        self._MAX_HEALTH = health

    def berserk_check(self, berserk):
        if berserk < 1:
            self.berserk = 1
        elif berserk > 2:
            self.berserk = 2
        else:
            self.berserk = berserk

    def attack(self):
        if self.weapon.critical_hit():
            return self.weapon.damage * self.berserk * 2
        else:
            return self.weapon.damage * self.berserk
