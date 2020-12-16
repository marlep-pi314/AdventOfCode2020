from pprint import pprint

NEARBY_TICKETS = 'nearby tickets'
MY_TICKET = 'your ticket'
SPECS = 'specs'

def format_input(filename):
    f = open(filename, "r")
    lines = [l.strip() for l in f.readlines()]
    f.close()

    puzzle_input = {NEARBY_TICKETS: []}
    puzzle_input[SPECS] = {}
    my_ticket = False
    nearby_tickets = False
    for line in lines:
        if 'or' in line:
            handle_specs(line, puzzle_input)
        elif len(line) == 0:
            continue
        elif MY_TICKET in line:
            my_ticket = True
        elif my_ticket:
            handle_my_ticket(line, puzzle_input)
            my_ticket = False
        elif NEARBY_TICKETS in line:
            nearby_tickets = True
        elif nearby_tickets:
            handle_nearby_tickets(line, puzzle_input)
        else:
            raise ValueError("none of the standard cases were met, SHOULD NOT HAPPEN")
    return puzzle_input


def handle_specs(line, puzzle_input):
    key_val = line.split(":")
    ranges = [int(x) for r in key_val[1].split("or") for x in r.strip().split("-")]
    puzzle_input[SPECS][key_val[0]] = ranges[:]


def handle_my_ticket(line, puzzle_input):
    puzzle_input[MY_TICKET] = [int(x) for x in line.split(",")]


def handle_nearby_tickets(line, puzzle_input):
    puzzle_input[NEARBY_TICKETS].append( [int(entry) for entry in line.split(",")] )


def collect_invalids(puzzle_input):
    invalids = []
    for ticket in puzzle_input[NEARBY_TICKETS]:
        for val in ticket:
            add_inavlid(val, invalids, puzzle_input)
    return invalids

def add_inavlid(value, invalids, puzzle_input):

    if not any([ puzzle_input[SPECS][k][0]<=value<=puzzle_input[SPECS][k][1] or  puzzle_input[SPECS][k][2]<= value <= puzzle_input[SPECS][k][3] for k in puzzle_input[SPECS].keys()]):
        invalids.append(value)
    

def get_ticket_scanning_error_rate(puzzle_input):
    return sum( collect_invalids(puzzle_input) )


if __name__ == '__main__':
    formatted_input = format_input("input")
    print("my ticket scanning error rate= {}".format(get_ticket_scanning_error_rate(formatted_input)))