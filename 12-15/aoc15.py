

def get_input(filename):
    f = open(filename, "r")
    lines = [l.strip() for l in f.readlines()]
    f.close()
    ret_list = [int(n) for n in lines[0].split(",")]
    return ret_list


def next_number(numbers):
    last = numbers[-1]
    # has it been spoken before?
    occurences = []
    for i in range(len(numbers)-1,-1,-1):
        if numbers[i]==last:
            occurences.append(i)
        if len(occurences)>1:
            break
    if len(occurences)>2 or len(occurences)==0:
        raise ValueError("there cannot be no or more than 2 occurences!!!")
    before = len(occurences)==2
    if before:
        numbers.append(max(occurences)-min(occurences))
    else:
        numbers.append(0)
    return numbers

# part II TODO:
def next_number_the_smart_way(numbers, already_seen):
    last = numbers[-1]
    if last in already_seen.keys():
        last_seen = already_seen[last]
        already_seen[last] = len(numbers)-1
        numbers.append(len(numbers)-1-last_seen)
    else:
        already_seen[last] = len(numbers)-1
        numbers.append(0)
    return numbers, already_seen

# def descent(numbers, search_no):
#     if not numbers:
#         return None
#     if numbers[-1] == search_no:
#         return len(numbers)-1
#     else:
#         return descent(numbers[:-1], search_no)


def get_all_up_to(count, inputfile, smart=False):
    numbers = get_input(inputfile)
    already_seen = {k:v for v,k in enumerate(numbers)}
    if not smart:
        while len(numbers)<count:
            next_number(numbers)
    else:
        while len(numbers)<count:
            numbers, already_seen = next_number_the_smart_way(numbers, already_seen)
    return numbers




if __name__ == '__main__':
    numbers = get_all_up_to(30000000, "input", smart=True)
    print("the {}th number is {}".format(len(numbers), numbers[-1]))
    # numbers = get_all_up_to(2020, "test_input", smart=True)
    # print("the {}th number is {}".format(len(numbers), numbers[-1]))
    # numbers = get_all_up_to(30000000, "input")
    # print("the {}th number is {}".format(len(numbers), numbers[-1]))