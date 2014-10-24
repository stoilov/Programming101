from orc import Orc
from weapon import Weapon
import unittest


class TestOrc(unittest.TestCase):

    def setUp(self):
        self.born_orc = Orc("Shapeshifter", 100, 1.5)

    def test_orc_init(self):
        self.assertEqual(self.born_orc.name, "Shapeshifter")
        self.assertEqual(self.born_orc.health, 100)
        self.assertEqual(self.born_orc.berserk, 1.5)

    def test_berserk_check_more(self):
        self.born_orc = Orc("Shapeshifter", 100, 3)
        self.assertEqual(self.born_orc.berserk, 2)

    def test_berserk_check_less(self):
        self.born_orc = Orc("Shapeshifter", 100, 0.2)
        self.assertEqual(self.born_orc.berserk, 1)

    def test_berserk_check(self):
        self.assertEqual(self.born_orc.berserk, 1.5)

    def test_attack(self):
        self.born_orc.weapon = Weapon("Mighty Axe", 20, 0.5)
        damages = set()
        for i in range(1000):
            damages.add(self.born_orc.attack())

        self.assertIn(30.0, damages)
        self.assertIn(60.0, damages)

if __name__ == '__main__':
    unittest.main()
