global fn_calls

f = open("input", "r")

fn_calls = 0

lines = sorted( [int(l) for l in f.readlines()] )

f.close()
index = len(lines)-1

def search_sum(left=0, right=index, total=2020):
    global fn_calls
    fn_calls += 1
    if left==right:
        return False
    sum = lines[left] + lines[right]
    if sum == total:
        print("no1 {}, no2 {}, product {}".format( lines[left], lines[right], lines[left]*lines[right]) )
        return  lines[left]*lines[right]
    elif sum > total :
        return search_sum(left=left, right=right-1, total=total)
    else:
        return search_sum(left=left+1, right=right, total=total)

#search_sum()

def triple():
    for x in range(0, index-1):
        a = search_sum(left=x+1, right=index, total=2020-lines[x])
        if a:
            print (lines[x], a*lines[x])
            break

triple()

print("-"*5)
print(fn_calls)