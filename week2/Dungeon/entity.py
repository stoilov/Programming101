class Entity:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self._MAX_HEALTH = health
        self.weapon = None

    def get_health(self):
        return self.health

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage_points):
        self.health -= damage_points
        if self.health <= 0:
            self.health = 0

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False

        if self.health + healing_points > self._MAX_HEALTH:
            self.health = self._MAX_HEALTH
        else:
            self.health += healing_points

        return True

    def has_weapon(self):
        if self.weapon is None:
            return False
        return True

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon.critical_hit():
            return self.weapon.damage * 2
        else:
            return self.weapon.damage
