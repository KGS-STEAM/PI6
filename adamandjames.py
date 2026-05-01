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
        
    

    
