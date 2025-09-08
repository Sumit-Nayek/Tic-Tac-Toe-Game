"""Minimax AI for Tic-Tac-Toe. Simple and clear implementation.
AI plays 'O' and human plays 'X'.
"""
from typing import List, Optional
from game.logic import available_moves, check_winner, is_draw

Board = List[str]


def minimax(board: Board, is_maximizing: bool) -> int:
# Terminal states
if check_winner(board, "O"):
return 1
if check_winner(board, "X"):
return -1
if is_draw(board):
return 0

if is_maximizing:
best_score = -999
for move in available_moves(board):
board[move] = "O"
score = minimax(board, False)
board[move] = ""
if score > best_score:
best_score = score
return best_score
else:
best_score = 999
for move in available_moves(board):
board[move] = "X"
score = minimax(board, True)
board[move] = ""
if score < best_score:
best_score = score
return best_score


def best_move(board: Board) -> Optional[int]:
moves = available_moves(board)
if not moves:
return None
best_score = -999
choice = None
for m in moves:
board[m] = "O"
score = minimax(board, False)
board[m] = ""
if score > best_score:
best_score = score
choice = m

return choice
import random
from .logic import check_winner

# Existing minimax and ai_move remain unchanged

def heuristic_ai_move(board):
    """A simpler, lower-difficulty AI using heuristics instead of minimax."""
    available_moves = [i for i, spot in enumerate(board) if spot == ""]

    # 1. Try to win
    for move in available_moves:
        test_board = board[:]
        test_board[move] = "O"
        if check_winner(test_board) == "O":
            return move

    # 2. Block opponent's winning move
    for move in available_moves:
        test_board = board[:]
        test_board[move] = "X"
        if check_winner(test_board) == "X":
            return move

    # 3. Otherwise, pick a random move
    return random.choice(available_moves)
