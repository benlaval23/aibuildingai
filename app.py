from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Tic Tac Toe board
board = [' '] * 9

# Function to check for a winner
def check_winner(board):
    winning_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]
    for position in winning_positions:
        if board[position[0]] == board[position[1]] == board[position[2]] != ' ':
            return board[position[0]]
    return None


# Function to check if the board is full
def is_board_full(board):
    return ' ' not in board

# Function to evaluate the minimax algorithm
def minimax(board, depth, is_maximizing):
    scores = {'X': -1, 'O': 1, 'tie': 0}

    if check_winner(board):
        if is_maximizing:
            return -1
        else:
            return 1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        max_score = float('-inf')
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                max_score = max(score, max_score)
        return max_score
    else:
        min_score = float('inf')
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                min_score = min(score, min_score)
        return min_score

# Route for the game page
@app.route('/')
def game():
    return render_template('game.html', board=board, check_winner=check_winner, is_board_full=is_board_full)

# Route to handle user moves
@app.route('/move', methods=['POST'])
def move():
    position = int(request.form['position'])
    if board[position] == ' ' and not check_winner(board) and not is_board_full(board):
        board[position] = 'X'
        if not check_winner(board) and not is_board_full(board):
            # Minimax algorithm makes a move
            best_score = float('-inf')
            best_move = -1
            for i in range(len(board)):
                if board[i] == ' ':
                    board[i] = 'O'
                    score = minimax(board, 0, False)
                    board[i] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = i
            board[best_move] = 'O'
    return redirect('/')

# Route to handle game reset
@app.route('/reset', methods=['POST'])
def reset():
    global board
    board = [' '] * 9
    return redirect('/')

if __name__ == '__main__':
    app.run(port=1234)

