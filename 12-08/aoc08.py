
f = open("input", "r")

lines = f.readlines()

f.close()

def format_input(lines):
    instructions = []
    for line in lines:
        l = line.split(" ")
        instructions.append( (l[0], int(l[1])) )
    return instructions


instructions = format_input(lines)


def run_code(instructions, from_line=0, acc=0, visited=None):
    globalvar = {'acc' : acc}
    if not visited:
        visited = []
    visited = visited[:]
    lnr = from_line
    while lnr < len(instructions) and lnr not in visited:
        if lnr not in visited:
            visited.append(lnr)
        lnr = execute(instructions[lnr], globalvar, lnr)
    return lnr, visited, globalvar
    print("finished on line {}, visited= {}, acc= {}".format(lnr+1, [l+1 for l in visited], globalvar['acc']))

    
def execute(instruction, globalvar, lnr):
    cmd, val = instruction
    if cmd == 'nop':
        return lnr+1
    elif cmd == 'jmp':
        return lnr + val
    globalvar[cmd] += val
    return lnr+1

# def correct_code(instructions):
#     lnr, visited, globalvar = run_code(instructions)

#     while lnr < len(instructions):
#         print(lnr, visited, lnr in visited, instructions[visited[-1]], globalvar)
#         cmd, val = instructions[visited[-1]]
#         if cmd == "jmp":
#             instructions[visited[-1]] = ("nop", val)
#         elif cmd == "nop":
#             instructions[visited[-1]] = ("jmp", val)
#         else:



#         lnr, visited, globalvar = run_code(instructions, from_line=visited[-1], acc=globalvar['acc'],visited=visited[:-1])
#         print(lnr, visited, lnr in visited, instructions[visited[-1]], globalvar)

def create_all(instructions):
    all_instructions = [instructions]
    index = 0
    while index < len(instructions):
        cmd, val = instructions[index]
        new_ins = []
        run = False
        if cmd == 'jmp':
            new_ins = instructions[:]
            new_ins[index] = ('nop', val)
            run = True
        elif cmd == 'nop':
            new_ins = instructions[:]
            new_ins[index] = ('jmp', val)
            run = True
        if run:
            lnr, visited, globalvar = run_code(new_ins)
            if lnr < len(new_ins):
                run = False
            else:
                print("Done {}".format(globalvar['acc']))
        index += 1

# print( run_code(instructions) )
create_all(instructions)
# correct_code(instructions)