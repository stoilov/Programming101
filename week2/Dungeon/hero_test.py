from hero import Hero
import unittest


class TestHero(unittest.TestCase):

    def setUp(self):
        self.born_hero = Hero("Bron", 100, "DragonSlayer")

    def test_hero_init(self):
        self.assertEqual(self.born_hero.name, "Bron")
        self.assertEqual(self.born_hero.health, 100)
        self.assertEqual(self.born_hero.nickname, "DragonSlayer")

    def test_known_as(self):
        self.assertEqual(self.born_hero.known_as(), "Bron the DragonSlayer")

if __name__ == '__main__':
    unittest.main()
