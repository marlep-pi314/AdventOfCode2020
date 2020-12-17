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
    to_remove = []
    for i, ticket in enumerate(puzzle_input[NEARBY_TICKETS]):
        for val in ticket:
            if add_to_invalids(val, invalids, puzzle_input):
                to_remove.append(i)

    return invalids, to_remove


def add_to_invalids(value, invalids, puzzle_input):
    if not any([ puzzle_input[SPECS][k][0]<=value<=puzzle_input[SPECS][k][1] or  puzzle_input[SPECS][k][2]<= value <= puzzle_input[SPECS][k][3] for k in puzzle_input[SPECS].keys()]):
        invalids.append(value)
        return True
    return False


def remove_invalids(puzzle_input):
    _, to_remove = collect_invalids(puzzle_input)
    # for ri in to_remove:
    #     print(puzzle_input[NEARBY_TICKETS][ri])
    puzzle_input[NEARBY_TICKETS] = [ticket for i, ticket in enumerate(puzzle_input[NEARBY_TICKETS]) if i not in to_remove]
    return puzzle_input


def check_all_tickets(puzzle_input):
    # loop through all tickets, check each one if it is valid
    invalids = []
    invalids_count = 0
    for i, ticket in enumerate(puzzle_input[NEARBY_TICKETS]):
        if not ticket_is_valid(ticket, puzzle_input[SPECS]):
            invalids.append(i)
            invalids_count += 1
    return invalids_count, invalids


def ticket_is_valid(ticket, specs):
    ticket_is_valid = True
    for i, value in enumerate(ticket):
        if not value_is_valid(value, specs):
            # this cannot be a valid ticket
            ticket_is_valid = False
            break
    return ticket_is_valid


def value_is_valid(value, specs):
    # loop over all ranges as defined per 'SPECS'
    # if false is returned then value does not fit in any category
    any_range = False
    for key in specs.keys():
        any_range = any_range or is_in_range( value, specs[key][0], specs[key][1], specs[key][2], specs[key][3])
    return any_range


def is_in_range(value, a, b, c, d):
    return a<=value<=b or c<=value<=d

def identify_fields(puzzle_input):
    possible_specs_keys = [key for key in puzzle_input[SPECS].keys()]
    # make a dic pointing pos in ticket to ALL possible ticket-fields
    dict_of_possibles = {k:possible_specs_keys[:] for k in range(len(puzzle_input[NEARBY_TICKETS][0]))}
    # now superficially remove all fields if any pos in tickets is out of range 
    for key in possible_specs_keys:
        for pos in range(len(puzzle_input[NEARBY_TICKETS][0])):
            if not ticket_pos_could_be(pos, puzzle_input, key):
                dict_of_possibles[pos].remove(key)
    # now we have limited each pos in a ticket to some possible fields.
    # however at least on pos has a unique field, therefore reduce them:
    processed_speckeys = []
    done = False
    while not done:
        # collect all which are len =1
        if len(processed_speckeys)==len(puzzle_input[SPECS].keys()):
            done = True
            continue
        position, key = [ (k, dict_of_possibles[k][0] ) for k in dict_of_possibles.keys() if len(dict_of_possibles[k])==1 and dict_of_possibles[k][0] not in processed_speckeys][0]
        # remove key from everywhere but pos:
        for pos in dict_of_possibles.keys():
            if pos == position:
                continue
            if key in dict_of_possibles[pos]:
                dict_of_possibles[pos].remove(key)
        # save this speckey - it is done 
        processed_speckeys.append(key)
    for k in dict_of_possibles.keys():
        dict_of_possibles[k] = dict_of_possibles[k][0]
    
    return dict_of_possibles

    # print("pos {} must be \'{}\'".format(pos, key))

    # now reduce
    # while any([ len(dict_of_possibles[k])>1 for k in dict_of_possibles.keys() ]):
    #     # reduce
    #     pass


def ticket_pos_could_be(pos, puzzle_input, specskey):
    valid = True
    for ticket in puzzle_input[NEARBY_TICKETS]:
        # a, b, c, d = puzzle_input[SPECS][specskey]
        valid = valid and is_in_range(ticket[pos], *puzzle_input[SPECS][specskey])
        if not valid:
            # one False is enough
            break
    return valid


def get_ticket_scanning_error_rate(puzzle_input):
    return sum( collect_invalids(puzzle_input)[0] )


def multiply_departure(puzzle_input):
    fieldsmap = identify_fields(puzzle_input)
    departure_list = [pos for pos in fieldsmap.keys() if 'departure' in fieldsmap[pos]]
    result = 1
    for pos in departure_list:
        result *= puzzle_input[MY_TICKET][pos]
    return result
    #ticket_index_list = [puzzle_input[SPECS] for ]


if __name__ == '__main__':
    formatted_input = format_input("input")
    print("my ticket scanning error rate= {}".format(get_ticket_scanning_error_rate(formatted_input)))
    
    
    puzzle_input = remove_invalids(formatted_input)
    # pprint(another_idea(puzzle_input))
    print("result of multiplication of all \'departure\' fields: {}".format(multiply_departure(puzzle_input)))