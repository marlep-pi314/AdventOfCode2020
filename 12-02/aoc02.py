
f = open("input", "r")

# read formatted input
input_lines = [line.split(":") for line in f.readlines()]

f.close()

# after split on :
def break_up_cond(str_cond):
    tmp = str_cond.split()
    cond_l = tmp[0].split("-")
    cond_lower, cond_upper = int(cond_l[0]), int(cond_l[1])
    cond_char = tmp[1].strip()
    return cond_lower, cond_upper, cond_char
    
def format_input(input_lines):
    processed = []
    for l in input_lines:
        cond, pw = l[0].strip(), l[1].strip()
        l, u, c = break_up_cond(cond)
        processed.append( {
            'min' : l,
            'max' : u,
            'char': c,
            'pw'  : pw
        })
    return processed

def validate(pw_dic):
    occ = pw_dic['pw'].count(pw_dic['char'])
    return pw_dic['min']<=occ<=pw_dic['max']

def tobbogan_validation(pw_dic):
    first = pw_dic['pw'][pw_dic['min']-1]==pw_dic['char']
    second = pw_dic['pw'][pw_dic['max']-1]==pw_dic['char']
    return first != second

def count_valid(processed_lines, vs='sled rental'):
    print("\'{}\' validation method".format(vs))
    if vs == 'tobbogan':
        return len([pw for pw in processed_lines if tobbogan_validation(pw)])
    return len([pw for pw in processed_lines if validate(pw)])


processed_data = format_input(input_lines)
print("{} of {} pw are valid.".format( count_valid(processed_data), len(input_lines)))
print("{} of {} pw are valid.".format( count_valid(processed_data, vs='tobbogan'), len(input_lines)))


# # testing
# #print("testing \'sled rental\':")
# # valid: 
# valid_string = "3-8 s: lswnfsjjdsh"
# print("{} (input \'{}\')".format( 1==count_valid(format_input([valid_string.split(":")])), valid_string))
# # invalid:
# invalid_string = "8-14 k: kkkkkkfkkkkkkkkk"
# print("{} (input \'{}\')".format( 0==count_valid(format_input([invalid_string.split(":")])), invalid_string))


# # testing
# #print('-'*10)
# #print("testing \'tobbogan\':")
# # valid: 
# valid_string = "3-8 s: lswnfsjsdsh"
# print("{} (input \'{}\')".format( 1==count_valid(format_input([valid_string.split(":")]), vs='tobbogan'), valid_string))
# # valid: 
# valid_string = "3-8 s: lssnfsjjdsh"
# print("{} (input \'{}\')".format( 1==count_valid(format_input([valid_string.split(":")]), vs='tobbogan'), valid_string))
# # invalid: 
# invalid_string = "3-8 s: lswnfsjjdsh"
# print("{} (input \'{}\')".format( 0==count_valid(format_input([invalid_string.split(":")]), vs='tobbogan'), invalid_string))
# # invalid:
# invalid_string = "8-14 k: kkkkkkfkkkkkkkkk"
# print("{} (input \'{}\')".format( 0==count_valid(format_input([invalid_string.split(":")]), vs='tobbogan'), invalid_string))