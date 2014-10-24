from fight import Fight
from orc import Orc
from hero import Hero
from weapon import Weapon
import unittest


class TestFight(unittest.TestCase):

    def setUp(self):
        self.hero = Hero("Bron", 100, "DragonSlayer")
        self.orc = Orc("Shapeshifter", 100, 1.5)
        sword = Weapon("Sword", 10, 0.2)
        axe = Weapon("Axe", 10, 0.2)
        self.hero.equip_weapon(sword)
        self.orc.equip_weapon(axe)
        self.battle = Fight(self.hero, self.orc)

    def test_fight_init(self):
        self.assertEqual(self.battle.hero.name, "Bron")
        self.assertEqual(self.battle.hero.health, 100)
        self.assertEqual(self.battle.hero.nickname, "DragonSlayer")
        self.assertEqual(self.battle.orc.name, "Shapeshifter")
        self.assertEqual(self.battle.orc.health, 100)
        self.assertEqual(self.battle.orc.berserk, 1.5)

    def test_flip_coin(self):
        flip_chances = set()
        for i in range(1000):
            flip_chances.add(self.battle.flip_coin())

        self.assertIn(True, flip_chances)
        self.assertIn(False, flip_chances)

    def test_simulate_fight_hero_first(self):
        entity_wins = set()
        for i in range(1000):
            self.battle.hero.health = 100
            self.battle.orc.health = 100
            entity_wins.add(self.battle.simulate_fight())

        self.assertIn("Hero wins.", entity_wins)
        self.assertIn("Orc wins.", entity_wins)


if __name__ == '__main__':
    unittest.main()
