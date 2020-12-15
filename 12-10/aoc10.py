import pprint

f = open("input", "r")

lines = [int(l) for l in f.readlines()]

f.close()


adapter_list = sorted(lines)
adapter_list.insert(0,0)
adapter_list.append( max(adapter_list)+3 )

bookkeep = {0:0,
            1:0,
            2:0,
            3:0}

def try_adapter(adapter, jolt):
    diff = adapter-jolt
    if 0 <= diff <= 3:
        # take this adapter (no need to look any further)
        jolt = adapter
        return diff, adapter
    return -1, jolt

def build_chain(adapter_list, bookkeep):
    bookkeep = bookkeep
    jolt = 0
    max_adapter_list = []
    i = 0
    max_adapter_list.append(jolt)
    while i<len(adapter_list):
        diff, jolt = try_adapter(adapter_list[i], jolt)
        if 0 <= diff <= 3:
            max_adapter_list.append(jolt) # append momentary jolt
            # next adapter is usable
            bookkeep[diff] += 1
            i += 1
        else:
            i += 1
    # finally increase bookkeep[3] by one because of device...
    bookkeep[3] += 1
    max_adapter_list.append(max_adapter_list[-1]+3)
    return max_adapter_list

def get_jolt_jumps(adapter_list):
    jump_list = [adapter_list[i]-adapter_list[i-1] for i in range(1,len(adapter_list))]
    occ_of_ones = 0
    occ_dic = {}
    for i in range(0,len(jump_list)):
        if jump_list[i] == 3:
            if occ_of_ones not in occ_dic:
                occ_dic[occ_of_ones] = 0
            occ_dic[occ_of_ones] += 1
            occ_of_ones = 0
        elif jump_list[i] == 1:
            occ_of_ones += 1
    return occ_dic, jump_list


counter = {'walkthrough' : 0}
# adapter_list is sorted
def walkthrough(adapter_list, index, counter, counter_key):
    MAX_LOOK_BACK = 3
    if index == 0:
        # print("index reached the end")
        counter[counter_key] += 1
        return True #done, yay, last adapter reached...?!
    jolt = adapter_list[index]
    
    # get all possibilities to move on
    next_up_jolt = [(i+max(0,index-MAX_LOOK_BACK), valid) for i, valid in enumerate(adapter_list[ max(0,index-MAX_LOOK_BACK): index]) if jolt <= valid + MAX_LOOK_BACK ]
    if not next_up_jolt or len(next_up_jolt)>3:
        raise Exception("EITHER NO NEXT OR TOO MANY")
    for pos, jlt in next_up_jolt:
        # if len(next_up_jolt)>1:
        #     print("choose ({},{})".format(pos, jlt))
        # print("pos {}, jolt {}".format(pos, jlt))
        walkthrough(adapter_list, pos, counter, counter_key)

# for first assignment we dont want 0 and max+3
short_adapter_list = adapter_list[1:-1]
max_adapter_list = build_chain(short_adapter_list, bookkeep)
print("product of 1-jolt and 3-jolt differences= {}".format(bookkeep[1]*bookkeep[3]))

occ_dic, jl = get_jolt_jumps(adapter_list)

for key in occ_dic.keys():
    if key == 0:
        continue
    adapter_list=[ i for i in range(0,key+1)]
    adapter_list.append( adapter_list[-1]+3 )
    if key not in counter:
        counter[key] = 0
    walkthrough(adapter_list, len(adapter_list)-1, counter, key)



result = 1
for key in counter.keys():
    if key in occ_dic.keys():
        result = result*counter[key]**occ_dic[key]
print("result {}, digits {}".format(result, len(str(result))))


# print( adapter_list[len(adapter_list)-1])


# max_adapter_list = build_chain(adapter_list, bookkeep)

# print(max_adapter_list)
# # für jeden 3er rang

        
