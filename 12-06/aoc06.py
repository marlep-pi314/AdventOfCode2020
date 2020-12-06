
f = open("input", "r")

lines = f.readlines()

f.close()


print("Hello world!")

if lines[-1] != '\n':
    lines.append('\n')


groups = []
group_str = ''
for l in lines:
    l = l.strip()
    if l:
        group_str += ' ' + l
    else:
        groups.append(group_str)
        group_str = ''

print("sum of yes-count= {}".format( sum([len(set(g.replace(" ", ""))) for g in groups])) )

sum_of_and_counts = 0 
for g in groups:
    gset = [set(e) for e in g.strip().split(" ")]
    inters = gset[0].intersection(*gset) 
    sum_of_and_counts += len(inters)

print("everzone \'yes\'-count {}".format(sum_of_and_counts))

