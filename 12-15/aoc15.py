

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
def next_number_the_smart_way(numbers):
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


def get_all_up_to(count, inputfile):
    numbers = get_input(inputfile)
    while len(numbers)<count:
        next_number(numbers)
    return numbers




if __name__ == '__main__':
    numbers = get_all_up_to(2020, "input")
    print("the {}th number is {}".format(len(numbers), numbers[-1]))
    numbers = get_all_up_to(30000000, "input")
    print("the {}th number is {}".format(len(numbers), numbers[-1]))