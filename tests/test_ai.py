from game.ai import best_move
from game.logic import create_empty_board

def test_ai_first_move():
board = create_empty_board()
move = best_move(board)
assert move in range(9)


def test_ai_blocks_win():
# Human about to win with X in positions 0 and 1
board = ["X", "X", "", "", "O", "", "", "", ""]
move = best_move(board)
# AI must block at position 2
assert move == 2


def test_ai_takes_win():
# AI has O in positions 0 and 1
board = ["O", "O", "", "X", "X", "", "", "", ""]
move = best_move(board)
# AI should win at position 2
assert move == 2