from hero import Hero
from orc import Orc
from fight import Fight


class Dungeon:

    def __init__(self, file_path):
        self.file_path = file_path
        self.spawned = {}

    def print_map(self):
        dungeon = open(self.file_path, "r")
        dungeon_map = dungeon.read()
        dungeon.close()
        return dungeon_map

    def spawn(self, player_name, entity):
        if type(entity) == Hero:
            on_map = "H"
        elif type(entity) == Orc:
            on_map = "O"
        else:
            return False

        dungeon = open(self.file_path, "r")
        field = dungeon.read()
        dungeon.close()
        if "S" in field:
            player_place = field.index("S")
            field = field.replace("S", on_map, 1)
            dungeon = open(self.file_path, "w")
            dungeon.write(field)
            dungeon.close()
            self.spawned[player_name] = [entity, player_place]
            return True
        return False

    def move(self, player_name, direction):
        if direction == "left":
            move_by = -1
        elif direction == "right":
            move_by = 1
        elif direction == "up":
            move_by = -11
        else:
            move_by = 11

        dungeon = open(self.file_path, "r")
        dungeon_map = dungeon.read()
        dungeon.close()
        dungeon_map = list(dungeon_map)
        new_place = self.spawned[player_name][1] + move_by
        out_of_map = new_place < 0 or new_place > len(dungeon_map) - 1
        if out_of_map or dungeon_map[new_place] in ["H", "O", "#", "\n"]:
            return False
        else:
            a = dungeon_map[new_place]
            dungeon_map[new_place] = dungeon_map[self.spawned[player_name][1]]
            dungeon_map[self.spawned[player_name][1]] = a
            self.spawned[player_name][1] += move_by
            dungeon_map = "".join(dungeon_map)
            dungeon = open(self.file_path, "w")
            dungeon.write(dungeon_map)
            dungeon.close()
            for player, info in self.spawned.items():
                into_right = self.spawned[player_name][1] == info[1] + 1
                into_left = self.spawned[player_name][1] == info[1] - 1
                into_up = self.spawned[player_name][1] == info[1] - 11
                into_down = self.spawned[player_name][1] == info[1] + 11
                into_enemy = into_right or into_left or into_up or into_down
                enemies = type(info[0]) != type(self.spawned[player_name][0])
                if into_enemy and enemies:
                    fight = Fight(info[0], self.spawned[player_name][0])
                    fight.simulate_fight()

            return True
