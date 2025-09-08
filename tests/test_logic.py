import pytest
from game.logic import create_empty_board, check_winner, is_draw, available_moves

def test_empty_board():
board = create_empty_board()
assert board == [""] * 9
assert available_moves(board) == list(range(9))
assert not check_winner(board, "X")
assert not is_draw(board)

def test_winner_rows():
board = ["X", "X", "X", "", "", "", "", "", ""]
assert check_winner(board, "X")


def test_winner_columns():
board = ["O", "", "", "O", "", "", "O", "", ""]
assert check_winner(board, "O")


def test_winner_diagonals():
board = ["X", "", "", "", "X", "", "", "", "X"]
assert check_winner(board, "X")


def test_draw():
board = ["X","O","X","X","O","O","O","X","X"]
assert is_draw(board)
assert not check_winner(board, "X")
assert not check_winner(board, "O")