from copy import deepcopy
from pprint import pprint

f = open("input", "r")
lines = [l.strip() for l in f.readlines()]

f.close()

WIDTH = len(lines[0])
HEIGHT = len(lines)

DIR = [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1)]

FLOOR = '.'
EMPTY = 'L'
OCCUPIED  = '#'

def format_input(lines):
    seats = []
    for l in lines:
        char_list = [c for c in l]
        seats.append(char_list) 
    return seats

PLAN = format_input(lines)
BACKUP_PLAN = PLAN[:]

def get_seat(x, y):
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        return None
    return PLAN[y][x]

def set_seat(x, y, value):
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        return None
    PLAN[y][x] = value

def get_neighbors(seats, x, y):
    ret_list = []
    x_range = [r for r in range(x-1, x+2) if r > -1 and r < WIDTH] 
    y_range = [r for r in range(y-1, y+2) if r > -1 and r < HEIGHT]
    for _x in x_range:
        for _y in y_range:
            if (_x != x or _y != y) and get_seat(_x, _y):
                ret_list.append((_x,_y))
    return ret_list

def get_neighbors_in_sight(x, y, debug=False):
    ret_list = []
    for dx, dy in DIR:
        for i in range(1,max(WIDTH,HEIGHT)):
            seat = get_seat(x+i*dx,y+i*dy)
            if not seat:
                break
            if debug:
                print("inspecting:".format(x+i*dx,y+i*dy))
            if seat == EMPTY or seat == OCCUPIED:
                ret_list.append( (x+i*dx,y+i*dy) )
                break
    return ret_list

# for the second problem
def should_change(seats, x, y):
    neightbors = get_neighbors_in_sight(x, y)
    # print(neightbors)
    nb_values = [get_seat(x, y) for (x,y) in neightbors]
    if get_seat(x, y) == OCCUPIED:
        if len([nb for nb in nb_values if nb == OCCUPIED]) > 4:
            # print("len > 3", [nb for nb in nb_values if nb == OCCUPIED])
            return True
    elif get_seat(x, y) == EMPTY:
        if len([nb for nb in nb_values if nb == OCCUPIED]) == 0:
            # print("len == 0", [nb for nb in nb_values if nb == OCCUPIED])
            return True
    return False

# this is for the first problem:
# def should_change(seats, x, y):
#     neightbors = get_neighbors(seats, x, y)
#     # print(neightbors)
#     nb_values = [get_seat(x, y) for (x,y) in neightbors]
#     if get_seat(x, y) == OCCUPIED:
#         if len([nb for nb in nb_values if nb == OCCUPIED]) > 3:
#             # print("len > 3", [nb for nb in nb_values if nb == OCCUPIED])
#             return True
#     elif get_seat(x, y) == EMPTY:
#         if len([nb for nb in nb_values if nb == OCCUPIED]) == 0:
#             # print("len == 0", [nb for nb in nb_values if nb == OCCUPIED])
#             return True
#     return False

def get_all_changes(seats):
    list_of_changes = []
    for x in range(0, WIDTH):
        for y in range(0,HEIGHT):
            if should_change(seats, x, y):
                list_of_changes.append( (x,y) )
    return list_of_changes

def advance_time(seats):
    list_of_changes = []
    for x in range(0,WIDTH):
        for y in range(0,HEIGHT):
            if should_change(seats, x, y):
                list_of_changes.append( (x,y) )
    apply_changes(seats, list_of_changes)
    return len(list_of_changes)>0

def apply_changes(seats, changes):
    for (x,y) in changes:
        if get_seat( x, y) == EMPTY:
            set_seat(x, y, OCCUPIED)
        elif get_seat(x, y) == OCCUPIED:
            set_seat(x, y, EMPTY)

def count_until_equilibrium(seats):
    timesteps = 0
    while advance_time(seats):
        timesteps += 1
    print("{} timesteps until equilibrium.".format(timesteps))

def count_occupied_seats(seats):
    return sum( [ row.count(OCCUPIED) for row in seats] )


def print_seats(seats):
    return '\n'.join(["".join(s) for s in seats])


PLAN = format_input(lines)

print(print_seats(PLAN))
# print("_"*80)
# advance_time(PLAN)
# print(print_seats(PLAN))

# print(should_change(PLAN, WIDTH-2, 0))
# print(get_neighbors_in_sight(WIDTH-2,0, debug=True))

# print("_"*80)
# advance_time(PLAN)
# print(print_seats(PLAN))

print("_"*80)
print("width {}, height {}".format(WIDTH, HEIGHT))

count_until_equilibrium(PLAN)

print("occupied seats {}".format(count_occupied_seats(PLAN) ))

