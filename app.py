import streamlit as st
from game.logic import (create_empty_board, check_winner, is_draw, available_moves)
from game.ai import best_move
# At the top, add import
from game.ai import ai_move, heuristic_ai_move

st.set_page_config(page_title="Tic-Tac-Toe AI", layout="centered")
st.title("🎮 Tic-Tac-Toe — Play vs AI")

# --- Session state initialization ---
if "board" not in st.session_state:
    st.session_state.board = create_empty_board()
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "message" not in st.session_state:
    st.session_state.message = "Your turn (X)!"
if "human_starts" not in st.session_state:
    st.session_state.human_starts = True

# Option to choose who starts
st.sidebar.title("Settings")
starter = st.sidebar.radio("Who starts?", ("Human (X)", "AI (O)"))
if starter == "Human (X)":
    st.session_state.human_starts = True
else:
    st.session_state.human_starts = False

# Reset button in sidebar
if st.sidebar.button("Reset"):
    st.session_state.board = create_empty_board()
    st.session_state.game_over = False
    st.session_state.message = "Your turn (X)!"
    st.experimental_rerun()

# If AI starts, let it make the first move (only once after a reset or setting change)
if not st.session_state.human_starts and not st.session_state.game_over and all(cell == "" for cell in st.session_state.board):
ai_choice = best_move(st.session_state.board)
if ai_choice is not None:
    st.session_state.board[ai_choice] = "O"

# Display board as 3 columns
cols = st.columns(3)
for i in range(9):
    label = st.session_state.board[i] if st.session_state.board[i] != "" else " "
# Disabled True for non-empty or game over
disabled = (st.session_state.board[i] != "") or st.session_state.game_over
if cols[i % 3].button(label, key=str(i), disabled=disabled):
# Human move
if not st.session_state.game_over and st.session_state.board[i] == "":
st.session_state.board[i] = "X"

# Check human win
if check_winner(st.session_state.board, "X"):
st.session_state.message = "🎉 You win!"
st.session_state.game_over = True
elif is_draw(st.session_state.board):
st.session_state.message = "😐 It's a draw!"
st.session_state.game_over = True
else:
# AI move
ai_choice = best_move(st.session_state.board)
if ai_choice is not None:
st.session_state.board[ai_choice] = "O"

if check_winner(st.session_state.board, "O"):
st.session_state.message = "🤖 AI wins!"
st.session_state.game_over = True
elif is_draw(st.session_state.board):
st.session_state.message = "😐 It's a draw!"
st.session_state.game_over = True

# Show board state visually as a simple grid of symbols below the buttons (read-only)
st.markdown("---")
st.markdown("**Board:**")
board_display = "\n".join([
" | ".join(st.session_state.board[r*3:(r+1)*3]) for r in range(3)
])
st.code(board_display)
st.caption("AI uses Minimax algorithm to play optimally. Click Reset from the sidebar to restart.")