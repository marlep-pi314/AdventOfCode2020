import itertools

f = open("input", "r")

lines = [int(i) for i in f.readlines()]

f.close()

def find_invalid(lines):
    preamble = 25
    i = 0
    while i<len(lines)-(preamble+1):
        found_any = any([ lines[x]+lines[y] == lines[i+preamble] for (x,y) in list(itertools.combinations(range(i,i+preamble), 2)) ])
        if not found_any:
            break
        i += 1
    return lines[i+preamble]


def partition(lines, invalid_number):
    index_list = []
    for i, no in enumerate(lines):
        if no < invalid_number-min(lines):
            index_list.append(i)
    return index_list


def scan_for_contiguous(index_list):
    list_of_startstop = []
    start_index = index_list[0]
    last_index = start_index
    for i, index in enumerate(index_list[1:]):
        if index - last_index > 1:
            if last_index - start_index >= 2:
                list_of_startstop.append( (start_index, last_index) )
            start_index = index
            last_index = index
        else:
            last_index = index
    return list_of_startstop


def search_set(lines, invalid_number, index_list):
    for (start, stop) in index_list[::-1]:
        for i in range(start, stop-1):
            for j in range(i+1, stop):
                if sum( lines[i:j+1] ) == invalid_number:
                    print("from {}, to {}".format(i, j))
                    return min(lines[i:j+1]) + max( lines[i:j+1] )
    return None


invalid_number = find_invalid(lines)
print("my invalid number {}".format(invalid_number) ) 
index_list = partition(lines, invalid_number)
smaller_index_list = scan_for_contiguous(index_list)
print(smaller_index_list)
print("resultsum {}".format(search_set(lines, invalid_number, smaller_index_list)))