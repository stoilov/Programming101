from random import randint
from weapon import Weapon


class Fight:

    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc

    def flip_coin(self):
        chance = randint(0, 100)
        hero_first = False
        if chance < 50:
            hero_first = True

        return hero_first

    def simulate_fight(self):
        hero_turn = self.flip_coin()
        while self.hero.health > 0 and self.orc.health > 0:
            if hero_turn:
                dmg = self.hero.attack()
                self.orc.take_damage(dmg)
            else:
                dmg = self.orc.attack()
                self.hero.take_damage(dmg)

            hero_turn = not hero_turn

        if not self.orc.is_alive():
            return "Hero wins."
        return "Orc wins."
