
import pprint

f = open("input", "r")
# f = open("input", "r")

lines = f.readlines()

f.close()


def format_input(lines):
    rules = {}
    for l in lines:
        r = l.split(" bags contain")
        values = [ b.strip() for b in r[1].split(",") ]
        go_to = {}
        for v in values:
            description = v.split(" ")
            if description[0].isdigit():
                go_to[description[1].strip()+' '+description[2].strip(' ')] = int(v[0])
            else:
                go_to['other'] = 0
        rules[r[0]] = go_to

    return rules

rules = format_input(lines)

def get_previous(reached, rules):
    ret_set = set()
    for k in rules.keys():
        if reached in rules[k].keys():
            ret_set.add(k)
    return ret_set

def collect_previous(from_set, rules):
    result = set()
    for element in set(from_set):
        result = result.union( get_previous(element, rules) )
    new_results = {elem for elem in result if elem not in from_set}
    
    if len(new_results)>0:
        return from_set.union(collect_previous(new_results, rules))
    return set()

def count_bags_in(bag, rules):
    if bag == 'other':
        return 1
    return sum( [int(rules[bag][bagtype]) + int(rules[bag][bagtype])*count_bags_in(bagtype, rules) for bagtype in rules[bag].keys()] )

    
bag = 'shiny gold'
count_bags_in(bag, rules)
print("{} contains: {}".format(bag, count_bags_in(bag, rules)) )





