from sense_hat import SenseHat, DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT, DIRECTION_MIDDLE
from random import randint
sense = SenseHat()
win = False
w = (255,255,255)
b = (0,0,0)
p = (140, 0 ,255)
r = (255,0,0)
bl = (0,0,255)
starting_board = [
b,b,w,b,b,w,b,b,
b,b,w,b,b,w,b,b,
w,w,w,w,w,w,w,w,
b,b,w,b,b,w,b,b,
b,b,w,b,b,w,b,b,
w,w,w,w,w,w,w,w,
b,b,w,b,b,w,b,b,
b,b,w,b,b,w,b,b
]
top_left = [0,1,8,9]
top_middle = [3,4,11,12]
top_right = [6,7,14,15]
middle_left = [24,25,32,33]
middle_middle = [27,28,35,36]
middle_right = [30,31,38,39]
bottom_left = [48,49,56,57]
bottom_middle = [51,52,59,60]
bottom_right = [54,55,62,63]
def position_2_number(position):
    if position == top_left:
        return 1
    elif position == top_middle:
        return 2
    elif position == top_right:
        return 3
    elif position == middle_left:
        return 4
    elif position == middle_middle:
        return 5
    elif position == middle_right:
        return 6
    elif position == bottom_left:
        return 7
    elif position == bottom_middle:
        return 8
    else:
        return 9
def number_to_position(placer_position):
    if placer_position == 1:
        return top_left
    elif placer_position == 2:
        return top_middle
    elif placer_position == 3:
        return top_right
    elif placer_position == 4:
        return middle_left
    elif placer_position == 5:
        return middle_middle
    elif placer_position == 6:
        return middle_right
    elif placer_position == 7:
        return bottom_left
    elif placer_position == 8:
        return bottom_middle
    elif placer_position == 9:
        return bottom_right
    
def placing(player):
    valid_space = False
    print(player + "'s turn")
    while valid_space == False:
        print("select your space must be between 1-9")
        selected_space = int(input())
        if selected_space >= 1 and selected_space <= 9:
            position = number_to_position(selected_space)
            checking_pixel = position[0]
            if starting_board(checking_pixel) == b:
                valid_space = True
            elif starting_board(checking_pixel) == b:
                print("That space is occupied select another.")
position = number_to_position(selected_space)

if player == red_player:
    clr = r
elif player == blue_player:
    clr = bl
    

starting_board.pop(position[0])
starting_board.insert(position[0],clr)
starting_board.pop(position[1])
starting_board.insert(position[1],clr)
starting_board.pop(position[2])
starting_board.insert(position[2],clr)
starting_board.pop(position[3])
starting_board.insert(position[3],clr)

sense.set_pixels(starting_board)

winning_sets = [123,456,789,147,258,369,159,753]
for item in winning_sets:
    set_total = 0
    for x in range(3):
        position = number_to_position(int(str(item)[x]))
        checking_pixel = position[0]
        if starting_board(int(checking_pixel)) == clr:
            set_total += 1
    if set_total == 3:
        print(player + "wins!")
        return True
    
draw_total = 0
for x in range (9):
    position = number_to_position(x+1)
    checking_pixel = position[0]
    if starting_board(checking_pixel) == bl or starting_board(checking_pixel) == r:
        draw total += 1
if draw_total == 9:
    print("It's a draw!")
elif draw_total != 9:
    return False


sense.set_pixels(starting_board)

print("Input name for player 1")
player1 = input()

    

