
f = open("input", "r")

lines = [ l.strip() for l in f.readlines()]

f.close()

ROWS = 128 
COLS = 8


def get_row_from_input(row_in, left=0, right=ROWS):
    if not row_in:
        return left
    elif row_in[0] == 'F':
        return  get_row_from_input(row_in[1:],left=left, right=left + int((right+1-left)/2)-1)
    else:
        return get_row_from_input(row_in[1:], left=left+int((right+1-left)/2), right=right)


def get_col_from_input(col_in, left=0, right=COLS):
    convert_str = col_in.replace("L", "F").replace("R", "B")
    return get_row_from_input(convert_str, left=left, right=right)


def get_seat(input_str):
    return get_row_from_input(input_str[:7]), get_col_from_input(input_str[7:])


def get_seat_identifier(input_str):
    r, c = get_seat(input_str) 
    return r, c, r*8 + c


def get_seat_from(sid):
    r = int(sid/8)
    c = sid % 8
    return r,c 


# complete_list = 
sorted_list = sorted([get_seat_identifier(l) for l in lines], key=lambda x: x[2])

sorted_id_list = [entry[2] for entry in sorted_list]

print("max= {}".format( sorted_id_list[-1] )) #996 result

for x in range(sorted_id_list[0]+1,sorted_id_list[-1]):
    if x not in sorted_id_list and x-1 in sorted_id_list and x+1 in sorted_id_list:
        print("your sid= {}".format(x)) 
