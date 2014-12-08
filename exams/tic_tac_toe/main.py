import copy


class Board:
    PLAYER = "O"
    AI = "X"
    ROW_LEN = 3
    grid_str = " {} | {} | {} \n___|___|___\n {} | {} | {}\n___|___|___\n {} | {} | {}\n   |   |   \n"

    def __init__(self):
        self.grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.player_turn = True
        self.ai_turn = False

    def get_empty_spots(self, grid):
        empty = []
        for row in range(3):
            for col in range(3):
                if grid[row][col] == " ":
                    empty.append([row, col])

        return empty

    def get_new_state(self, grid, move):
        if self.player_turn:
            grid[move[0]][move[1]] = Board.PLAYER
        else:
            grid[move[0]][move[1]] = Board.AI

        return grid

    def minimax(self, grid, depth):
        if self.is_game_over():
            return self.score(grid, depth)

        depth += 1
        scores = []
        moves = []

        for move in self.get_empty_spots(grid):
            possible_game = self.get_new_state(grid, move)
            if self.game_win(possible_game, Board.AI) or self.game_win(possible_game, Board.PLAYER):
                return move

            scores.append(self.score(possible_game, depth))
            moves.append(move)

        if self.player_turn:
            max_score_index = scores.index(max(scores))
            move = moves[max_score_index]
            return move
        else:
            min_score_index = scores.index(min(scores))
            move = moves[min_score_index]
            return move

    def game_win(self, grid, participant):
        for row in grid:
            if row.count(participant) == Board.ROW_LEN:
                return True

        transposed = [[row[i] for row in grid] for i in range(Board.ROW_LEN)]
        for row in transposed:
            if row.count(participant) == Board.ROW_LEN:
                return True

        main_diagonal = [grid[row][row] for row in range(Board.ROW_LEN)]
        if main_diagonal.count(participant) == Board.ROW_LEN:
                return True

        other_diagonal = [grid[row][2 - row] for row in range(Board.ROW_LEN)]
        if other_diagonal.count(participant) == Board.ROW_LEN:
                return True
        return False

    def score(self, board, depth):
        if self.game_win(board, Board.PLAYER):
            return 10 - depth
        elif self.game_win(board, Board.AI):
            return depth - 10
        else:
            return 0

    def is_game_over(self):
        grid_elements = [row[i] for row in self.grid for i in range(Board.ROW_LEN)]
        if " " in grid_elements:
            return False
        return True

    def make_player_turn(self):
        while True:
            try:
                row = int(input("Select row: "))
                col = int(input("Select col: "))
                break
            except Exception:
                print("Only integer values are accepted.")

        return row-1, col-1


def main():
    board = Board()
    grid_print_list = [row[i] for row in board.grid for i in range(Board.ROW_LEN)]
    print(Board.grid_str.format(*grid_print_list))
    while not board.is_game_over():
        board.grid = board.get_new_state(board.grid, board.make_player_turn())
        grid_copy = copy.deepcopy(board.grid)
        new_minimax = board.minimax(board.grid, 0)
        board.player_turn, board.ai_turn = board.ai_turn, board.player_turn
        print(new_minimax)
        board.grid = board.get_new_state(grid_copy, new_minimax)
        board.player_turn, board.ai_turn = board.ai_turn, board.player_turn
        grid_print_list = [row[i] for row in board.grid for i in range(Board.ROW_LEN)]
        print(Board.grid_str.format(*grid_print_list))
        if board.game_win(board.grid, Board.PLAYER):
            print("Congratulations! You win!")
            break
        if board.game_win(board.grid, Board.AI):
            print("You lose!")
            break
    else:
        print("It's a draw.")

if __name__ == '__main__':
    main()
