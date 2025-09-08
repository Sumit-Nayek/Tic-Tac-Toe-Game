"""Game logic for Tic-Tac-Toe: board helpers and win/draw checks.
Board representation: a list of length 9 with values: "" (empty), "X", or "O".
Indices map as:
0 1 2
3 4 5
6 7 8
"""

from typing import List

Board = List[str]

WIN_LINES = [
[0,1,2], [3,4,5], [6,7,8], # rows
[0,3,6], [1,4,7], [2,5,8], # cols
[0,4,8], [2,4,6] # diagonals
]

def create_empty_board() -> Board:
return [""] * 9

def available_moves(board: Board) -> List[int]:
return [i for i, v in enumerate(board) if v == ""]

def check_winner(board: Board, player: str) -> bool:
for line in WIN_LINES:
if all(board[pos] == player for pos in line):
return True
return False

def is_draw(board: Board) -> bool:
return all(cell != "" for cell in board)