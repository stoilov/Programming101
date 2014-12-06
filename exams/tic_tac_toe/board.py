import copy


class Board:
    player = "O"
    ai = "X"
    grid_str = " {} | {} | {} \n___|___|___\n {} | {} | {}\n___|___|___\n {} | {} | {}\n   |   |   \n"

    def __init__(self):
        self.depth = 0
        self.grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        # self.grid = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

    def have_winner(self, turn_taker, grid):
        for row in grid:
            if row.count(turn_taker) == 3:
                return True

        transposed = [[row[i] for row in grid] for i in [0, 1, 2]]
        for row in transposed:
            if row.count(turn_taker) == 3:
                return True

        main_diagonal = [grid[row][row] for row in [0, 1, 2]]
        if main_diagonal.count(turn_taker) == 3:
                return True

        other_diagonal = [grid[row][2 - row] for row in [0, 1, 2]]
        if other_diagonal.count(turn_taker) == 3:
                return True
        return False

    def get_empty_spots(self, grid):
        empty = []
        for row, element_row in enumerate(grid):
            for col, element_col in enumerate(grid):
                if grid[row][col] == " ":
                    empty.append((row, col))

        return empty

    def put_mark_ai(self, coordinate, grid):
        grid[coordinate[0]][coordinate[1]] = Board.ai
        return grid

    def put_mark_player(self, coordinate, grid):
        grid[coordinate[0]][coordinate[1]] = Board.player
        return grid

    def minimax(self, turn_taker, grid, depth):
        scores = []
        grid_elements = [row[i] for row in grid for i in [0, 1, 2]]
        while " " in grid_elements:
            grid_copy = copy.deepcopy(grid)
            depth += 1
            for spot in self.get_empty_spots(grid):
                if turn_taker == Board.player:
                    grid_copy = self.put_mark_ai(spot, grid_copy)
                else:
                    grid_copy = self.put_mark_player(spot, grid_copy)

                if self.have_winner(turn_taker, grid_copy):
                    if turn_taker == Board.player:
                        score = 10 - depth
                    else:
                        score = -10 + depth

                    scores.append({"grid": grid, "score": score})
                else:
                    if turn_taker == Board.player:
                        new_taker = Board.ai
                    else:
                        new_taker = Board.player

                    self.minimax(new_taker, grid_copy, depth)
        return scores


def main():
    board = Board()
    board_list = [row[i] for row in board.grid for i in [0, 1, 2]]
    print(Board.grid_str.format(*board_list))
    board.have_winner("O")

if __name__ == '__main__':
    main()
