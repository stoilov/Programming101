from entity import Entity
from weapon import Weapon
import unittest


class TestEntity(unittest.TestCase):

    def setUp(self):
        self.born_entity = Entity("Shapeshifter", 100)

    def test_entity_init(self):
        self.assertEqual(self.born_entity.name, "Shapeshifter")
        self.assertEqual(self.born_entity.health, 100)

    def test_get_health(self):
        self.assertEqual(self.born_entity.get_health(), 100)

    def test_is_alive(self):
        self.assertTrue(self.born_entity.is_alive())

    def test_is_alive_dead(self):
        self.born_entity.health = 0
        self.assertFalse(self.born_entity.is_alive())

    def test_take_damage(self):
        damage = 20
        self.born_entity.take_damage(damage)
        self.assertEqual(self.born_entity.health, 80)

    def test_take_damage_float(self):
        damage = 20.5
        self.born_entity.take_damage(damage)
        self.assertEqual(self.born_entity.health, 79.5)

    def test_take_damage_more(self):
        damage = 120
        self.born_entity.take_damage(damage)
        self.assertEqual(self.born_entity.health, 0)

    def test_take_healing_is_dead(self):
        self.born_entity.health = 0
        healing_points = 20
        self.assertFalse(self.born_entity.take_healing(healing_points))
        self.assertEqual(self.born_entity.health, 0)

    def test_take_healing(self):
        healing_points = 10
        self.assertTrue(self.born_entity.take_healing(healing_points))
        self.assertEqual(self.born_entity.health, 100)

    def test_take_healing_add(self):
        self.born_entity.health = 70
        healing_points = 20
        self.assertTrue(self.born_entity.take_healing(healing_points))
        self.assertEqual(self.born_entity.health, 90)

    def test_has_weapon_no(self):
        self.assertFalse(self.born_entity.has_weapon())

    def test_has_weapon_yes(self):
        self.born_entity.weapon = Weapon("Mighty Axe", 25, 0.2)
        self.assertTrue(self.born_entity.has_weapon())

    def test_equip_weapon(self):
        weapon = Weapon("Mighty Axe", 25, 0.2)
        self.born_entity.equip_weapon(weapon)
        self.assertEqual(self.born_entity.weapon, weapon)

    def test_attack(self):
        self.born_entity.weapon = Weapon("Mighty Axe", 25, 0.5)
        damages = set()
        for i in range(1000):
            damages.add(self.born_entity.attack())

        self.assertIn(25, damages)
        self.assertIn(50, damages)

if __name__ == '__main__':
    unittest.main()
