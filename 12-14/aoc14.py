
from itertools import product
from pprint import pprint

def format_input(inputfile):
    f = open(inputfile, "r")
    lines = [l.strip() for l in f.readlines()]
    f.close()
    tuple_list = []
    for l in lines:
        key_val = l.split(" = ")
        if 'mask' in key_val[0]:
            tuple_list.append( (key_val[0], key_val[1]) )
        elif 'mem' in key_val[0]:
            tuple_list.append( (int( key_val[0][4:-1] ), int(key_val[1])) )
    return tuple_list


def apply_mask(mask, amount, bit=36):
    str_rep = to_str_wrt_bits(amount, bit=bit)
    ret_str = ''
    for i, c in enumerate(mask):
        if c=='X':
            ret_str += str_rep[i]
        else:
            ret_str += c
    return ret_str


def apply_mask_v2(mask, addr, bit=36):
    # print("adddr {}".format(addr))
    addr_as_str = to_str_wrt_bits(addr, bit=bit)
    wildcard_str = ''
    for i, c in enumerate(mask):
        if c=='X':
            wildcard_str += 'X'
        elif c == '0':
            wildcard_str += addr_as_str[i]
        else:
            wildcard_str += c
    ###print(wildcard_str)
    return wildcard_str


def get_addr_combos(wildcard_str):
    count_x = wildcard_str.count('X')
    # print(wildcard_str, count_x)
    addr_list = [ wildcard_str[:] for i in range(2**count_x)]
    combos = [c for c in product([0,1], repeat=count_x)]
    wildcard_str
    # for c in combos:
    #     print(c)
    for i, adr in enumerate(addr_list):
        addr_list[i] = adr.split("X")
    len(addr_list[0])
    len(combos[0])
    for i, adrl in enumerate(addr_list):
        addr_list[i] = "".join([adrl[j]+str(combos[i][j]) for j in range(0,len(combos[i]))]+[adrl[-1]])
    # now addr_list contains all combinations for 'X's
    ###print("\n".join(addr_list))
    return addr_list


def run_v2(inputfile):
    formatted_in = format_input(inputfile)
    mem = {}
    mask = ''
    for k, v in formatted_in:
        if k == 'mask':
            mask = v[:]
        else:
            #print("applying mask {} to K{}".format(mask, k))
            addr_list = get_addr_combos(apply_mask_v2(mask, k))
            for a in addr_list:
                mem[to_int(a)] = v
    return mem


def run_input(inputfile):
    formatted_in = format_input(inputfile)
    mem = {}
    mask = ''
    for k, v in formatted_in:
        if k == 'mask':
            mask = v[:]
        else:
            mem[k] = to_int( apply_mask(mask, v))
    return mem


def sum_of_mem_addr(mem):
    return sum([ mem[k] for k in mem.keys()])


def to_int(x):
    return sum([int(c)*2**i for i, c in enumerate(x[::-1])])


def to_str(x):
    if x>1:
        return to_str(x//2) + str(x%2)
    else:
        return str(x%2)

def to_str_wrt_bits(x, bit=36):
    x_as_str = to_str(x)
    return "0"*(bit-len(x_as_str))+x_as_str


if __name__ == '__main__':
    # memory = run_input("input")
    # print(sum_of_mem_addr(memory))
    # memory = run_v2("test_input2")
    # print(sum_of_mem_addr(memory))
    
    memory = run_v2("input")
    print(sum_of_mem_addr(memory))
    # pprint(memory)