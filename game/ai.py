"""
Minimax AI for Tic-Tac-Toe.
AI plays 'O' and human plays 'X'.
Simple, clear, and fixed version.
"""

from typing import List, Optional
import random

# -----------------------------
# Helper Functions
# -----------------------------

Board = List[str]

WIN_COMBINATIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

def check_winner(board: Board, player: str) -> bool:
    return any(all(board[i] == player for i in line) for line in WIN_COMBINATIONS)

def is_draw(board: Board) -> bool:
    return "" not in board and not check_winner(board, "X") and not check_winner(board, "O")

def available_moves(board: Board) -> List[int]:
    return [i for i, cell in enumerate(board) if cell == ""]

# -----------------------------
# Minimax Algorithm
# -----------------------------

def minimax(board: Board, is_maximizing: bool) -> int:
    # Base / terminal conditions
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_draw(board):
        return 0

    # Maximizing for AI ('O')
    if is_maximizing:
        best_score = -999
        for move in available_moves(board):
            board[move] = "O"
            score = minimax(board, False)
            board[move] = ""
            best_score = max(best_score, score)
        return best_score
    else:
        # Minimizing for Human ('X')
        best_score = 999
        for move in available_moves(board):
            board[move] = "X"
            score = minimax(board, True)
            board[move] = ""
            best_score = min(best_score, score)
        return best_score

# -----------------------------
# Find Best Move for AI
# -----------------------------

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

# -----------------------------
# Simpler Heuristic AI
# -----------------------------

def heuristic_ai_move(board: Board) -> int:
    """A simpler AI using heuristics instead of full minimax."""
    moves = available_moves(board)

    # 1. Try to win
    for move in moves:
        test_board = board[:]
        test_board[move] = "O"
        if check_winner(test_board, "O"):
            return move

    # 2. Block opponent's winning move
    for move in moves:
        test_board = board[:]
        test_board[move] = "X"
        if check_winner(test_board, "X"):
            return move

    # 3. Otherwise, pick a random move
    return random.choice(moves)
