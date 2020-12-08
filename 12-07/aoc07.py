
import pprint

f = open("input", "r")

lines = f.readlines()

f.close()


def format_input(lines):
    rules = {}
    for l in lines:
        r = l.split("contain")
        rules[r[0]] = [ b.strip() for b in r[1].split(",") ]
    return rules
rules = format_input(lines)


def get_previous(reached, rules):
    return [ k for k in rules.keys() if reached[:-1] in ' '.join(rules[k])]

def collect_previous(from_list, rules):
    start_count = len(from_list)
    print("round {}".format(start_count))
    result = set(from_list)
    for element in set(from_list):
        # print("get_element:")
        # pprint.pprint(get_previous(element, rules))
        result = result.union( set(get_previous(element, rules)).union(set(from_list)) ).copy()
    print("current result")
    pprint.pprint(result)
    
    from_list = list(result)
    
    if start_count < len(from_list):
        return collect_previous(from_list, rules)
    else:
        return from_list
         
directly = []
for k in rules.keys():
    if 'shiny gold' in ' '.join(rules[k]):
        directly.append(k)

results = collect_previous(['shiny gold'], rules)
#pprint.pprint(results)

#pprint.pprint(rules)





# directly = get_previous('shiny gold', rules)

# endresult = collect_previous(directly, rules)

# print("there are {} different bags?!".format(len(rules.keys())))
print("{} different bags may contain a \'shiny golden\' bag".format(len(results)))




