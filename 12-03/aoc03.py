
f = open("input", "r")

lines = [line.strip() for line in f.readlines()]

f.close()

# directions x+3, y+1

# lines[y][x]

# mod = len(lines[0])
# y_lim = len(lines)
# x=3

# dx = 3
# dy = 1

# tree = 0
# free = 0
# for y in range(1,y_lim,dy):
#     if lines[y][x] == '#':
#         tree += 1
#     else:
#         free += 1
#     x = (x + dx)%mod

def count_trees(slope, lines):
    dx, dy = slope
    mod = len(lines[0])
    y_lim = len(lines)
    x=0
    tree = 0
    for y in range(0,y_lim,dy):
        if lines[y][x] == '#':
            tree += 1
        x = (x + dx)%mod
    return tree

print("trees encountered {}".format(count_trees((3,1), lines)))

product = 1
for slope in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    count = count_trees(slope, lines)
    print("slope= {}, trees encountered {}".format(slope, count))
    product *= count
print("product= {}".format(product))

# slope = (3,1)in
# slope = (1,1)
# print("slope= {}, trees encountered {}".format(slope, count_trees(slope, lines)))
# slope = (5,1)
# print("slope= {}, trees encountered {}".format(slope, count_trees(slope, lines)))
# slope = (7,1)
# print("slope= {}, trees encountered {}".format(slope, count_trees(slope, lines)))
# slope = (1,2)
# print("slope= {}, trees encountered {}".format(slope, count_trees(slope, lines)))