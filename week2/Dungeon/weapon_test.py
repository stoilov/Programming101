from weapon import Weapon
import unittest


class TestWeapon(unittest.TestCase):

    def setUp(self):
        self.axe = Weapon("Mighty Axe", 25, 0.2)

    def test_weapon_init(self):
        self.assertEqual(self.axe.type, "Mighty Axe")
        self.assertEqual(self.axe.damage, 25)
        self.assertEqual(self.axe.critical_strike_percent, 0.2)

    def test_value_error(self):
        with self.assertRaises(ValueError):
            Weapon("Mighty Axe", 25, 2)

    def test_critical_hit(self):
        has_been_true = False
        has_been_false = False
        for i in range(1000):
            if self.axe.critical_hit():
                has_been_true = True
            else:
                has_been_false = True

        self.assertTrue(has_been_true)
        self.assertTrue(has_been_false)


if __name__ == '__main__':
    unittest.main()
