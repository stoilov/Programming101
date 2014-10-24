import unittest
from dungeon import Dungeon
from orc import Orc
from hero import Hero
from weapon import Weapon
import os


class TestDungeon(unittest.TestCase):
    def setUp(self):
        self.filename = 'dungeon.txt'
        self.file_to_read = open(self.filename, 'w')
        field = ["S.##......", "#.##..###.", "#.###.###.", "#.....###.", "###.#####S"]
        self.file_to_read.write("\n".join(field))
        self.file_to_read.close()
        self.dungeon = Dungeon("dungeon.txt")

    def tearDown(self):
        os.remove(self.filename)

    def test_dungeon_init(self):
        self.assertEqual(self.dungeon.file_path, "dungeon.txt")

    def test_print_map(self):
        dungeon = self.dungeon.print_map()
        this_map = "S.##......\n#.##..###.\n#.###.###.\n#.....###.\n###.#####S"
        self.assertEqual(dungeon, this_map)

    def test_spawn(self):
        boromir = Hero("Boromir", 100, "OneDoesNotSimply")
        gollum = Orc("Gollum", 100, 1.5)

        spawns = set()
        spawns.add(self.dungeon.spawn("player_1", boromir))
        spawns.add(self.dungeon.spawn("player_2", gollum))
        self.assertDictEqual({"player_1": [boromir, 0], "player_2": [gollum, 53]}, self.dungeon.spawned)
        self.assertIn(True, spawns)

    def test_spawn_no_more_space(self):
        boromir = Hero("Boromir", 100, "OneDoesNotSimply")
        gollum = Orc("Gollum", 100, 1.5)
        bilbo = Hero("Bilbo", 100, "Baggins")

        spawns = set()
        spawns.add(self.dungeon.spawn("player_1", boromir))
        spawns.add(self.dungeon.spawn("player_2", gollum))
        spawns.add(self.dungeon.spawn("player_3", bilbo))
        self.assertDictEqual({"player_1": [boromir, 0], "player_2": [gollum, 53]}, self.dungeon.spawned)
        self.assertIn(False, spawns)

    def test_move_right(self):
        boromir = Hero("Boromir", 100, "OneDoesNotSimply")
        self.dungeon.spawn("player_1", boromir)
        move_entity = self.dungeon.move("player_1", "right")
        self.assertTrue(move_entity)
        self.assertEqual(self.dungeon.spawned["player_1"][1], 1)

    def test_move_down(self):
        boromir = Hero("Boromir", 100, "OneDoesNotSimply")
        self.dungeon.spawn("player_1", boromir)
        self.dungeon.move("player_1", "right")
        move_entity = self.dungeon.move("player_1", "down")
        self.assertTrue(move_entity)

    def test_move_left(self):
        boromir = Hero("Boromir", 100, "OneDoesNotSimply")
        self.dungeon.spawn("player_1", boromir)
        self.dungeon.move("player_1", "right")
        move_entity = self.dungeon.move("player_1", "left")
        self.assertTrue(move_entity)

    def test_move_up(self):
        boromir = Hero("Boromir", 100, "OneDoesNotSimply")
        self.dungeon.spawn("player_1", boromir)
        self.dungeon.move("player_1", "right")
        self.dungeon.move("player_1", "down")
        move_entity = self.dungeon.move("player_1", "up")
        self.assertTrue(move_entity)

    def test_move_left_no_where_to_go(self):
        boromir = Hero("Boromir", 100, "OneDoesNotSimply")
        self.dungeon.spawn("player_1", boromir)
        move_entity = self.dungeon.move("player_1", "left")
        self.assertFalse(move_entity)

    def test_move_up_no_where_to_go(self):
        boromir = Hero("Boromir", 100, "OneDoesNotSimply")
        self.dungeon.spawn("player_1", boromir)
        move_entity = self.dungeon.move("player_1", "up")
        self.assertFalse(move_entity)

    def test_move_right_no_where_to_go(self):
        boromir = Hero("Boromir", 100, "OneDoesNotSimply")
        gollum = Orc("Gollum", 100, 1.5)
        self.dungeon.spawn("player_1", boromir)
        self.dungeon.spawn("player_2", gollum)
        move_entity = self.dungeon.move("player_2", "right")
        self.assertFalse(move_entity)

    def test_move_down_no_where_to_go(self):
        boromir = Hero("Boromir", 100, "OneDoesNotSimply")
        gollum = Orc("Gollum", 100, 1.5)
        self.dungeon.spawn("player_1", boromir)
        self.dungeon.spawn("player_2", gollum)
        move_entity = self.dungeon.move("player_2", "down")
        self.assertFalse(move_entity)

    def test_move_and_fight(self):
        boromir = Hero("Boromir", 100, "OneDoesNotSimply")
        gollum = Orc("Gollum", 100, 1.5)
        axe = Weapon("Mighty Axe", 25, 0.2)
        sword = Weapon("Sword", 25, 0.2)
        boromir.equip_weapon(sword)
        gollum.equip_weapon(axe)
        self.dungeon.spawn("player_1", boromir)
        self.dungeon.spawn("player_2", gollum)
        self.dungeon.spawned["player_2"][1] = 12
        self.dungeon.move("player_1", "right")
        been_fight = self.dungeon.spawned["player_1"][0].is_alive() and self.dungeon.spawned["player_2"][0].is_alive()
        self.assertFalse(been_fight)

if __name__ == '__main__':
    unittest.main()
