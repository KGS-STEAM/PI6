from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

# Colours
X_COLOR = (255, 0, 0)      # Red
O_COLOR = (0, 0, 255)      # Blue
CURSOR  = (0, 255, 0)      # Green

EMPTY   = (0, 0, 0)        # Black


# 3×3 board stored as characters
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

cursor_r = 1
cursor_c = 1
player = "X"

def draw_board():
    pixels = [EMPTY] * 64

    # draw pieces
    for r in range(3):
        for c in range(3):
            idx = r * 8 + c
            if board[r][c] == "X":
                pixels[idx] = X_COLOR
            elif board[r][c] == "O":
                pixels[idx] = O_COLOR

    # draw cursor
    cursor_idx = cursor_r * 8 + cursor_c
    pixels[cursor_idx] = CURSOR

    sense.set_pixels(pixels)

def check_winner():
    # rows
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] != " ":
            return board[r][0]

    # columns
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != " ":
            return board[0][c]

    # diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def full():
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                return False
    return True

def reset():
    global board, cursor_r, cursor_c, player
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    cursor_r = 1
    cursor_c = 1
    player = "X"
    sense.clear()

# MAIN LOOP
while True:
    draw_board()
    event = sense.stick.wait_for_event()

    if event.action == "pressed":

        # move cursor
        if event.direction == "up":
            cursor_r = (cursor_r - 1) % 3
        elif event.direction == "down":
            cursor_r = (cursor_r + 1) % 3
        elif event.direction == "left":
            cursor_c = (cursor_c - 1) % 3
        elif event.direction == "right":
            cursor_c = (cursor_c + 1) % 3

        # place X or O
        elif event.direction == "middle":
            if board[cursor_r][cursor_c] == " ":
                board[cursor_r][cursor_c] = player

                winner = check_winner()
                if winner:
                    draw_board()
                    sense.show_message(f"{winner} wins!", scroll_speed=0.05)
                    sense.show_message("Press to restart", scroll_speed=0.05)
                    sense.stick.wait_for_event()
                    reset()
                    continue

                if full():
                    draw_board()
                    sense.show_message("Draw!", scroll_speed=0.05)
                    sense.show_message("Press to restart", scroll_speed=0.05)
                    sense.stick.wait_for_event()
                    reset()
                    continue

                # switch player
               
               


player = "O" if player == "X" else "X"
 
 
 
 
















































