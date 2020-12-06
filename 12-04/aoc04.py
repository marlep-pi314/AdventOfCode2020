
f = open("input", "r")


lines = f.readlines()

f.close()

if lines[-1] != '\n':
    lines.append('\n')

PP_KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

_list = [l for l in lines if l=='\n']
passportcount = len(_list)

def handle_ppin(alist, index):
    fields = []
    for l in alist:
        fields.extend(l.strip().split(' '))
    return fields

def valid_year(yr, inputstr):
    if not inputstr.isdigit():
        return False#
    year = int(inputstr)
    if yr=='byr':
        return 1920<=year<=2002
    elif yr=='iyr':
        return 2010<=year<=2020
    elif yr=='eyr':
        return 2020<=year<=2030
    return False

def valid_height(inputstr):
    num = inputstr[:-2]
    if not num.isdigit():
        return False
    num = int(num)

    unit = inputstr[-2:]
    if 'cm' != unit and 'in' != unit:
        return False
    
    if unit == 'cm':
        return 150<=num<=193
    elif unit == 'in':
        return 59<=num<=76
    else:
        return False

def valid_hair(inputstr):
    if '#' != inputstr[0]:
        return False
    hairclr = inputstr[1:]
    if len(hairclr)!=6:
        return False
    for c in hairclr:
        if c not in '0123456789abcdef':
            return False
    return True

def valid_eye(inputstr):
    allowed = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return len([clr for clr in allowed if clr == inputstr])==1

def valid_pid(inputstr):
    if not inputstr.isdigit():
        return False
    return len(inputstr)==9

def validate_fields( fields ):
    passport = {}
    # return pp dict if valid, False sonst
    _missing_list = [ field for field in PP_KEYS if field not in ' '.join(fields)]
    if (not _missing_list) or ['cid'] == _missing_list:
        for f in fields:
            kvp = f.split(':')
            passport[kvp[0]]=kvp[1]
        return passport
    return False

def scrutinize(pp):
    # check years
    check_key = 'byr'
    if not valid_year(check_key, pp[check_key]):
        return False
    check_key = 'iyr'
    if not valid_year(check_key, pp[check_key]):
        return False
    check_key = 'eyr'

    if not valid_year(check_key, pp[check_key]):
        return False
    # height
    check_key = 'hgt'
    if not valid_height(pp[check_key]):
        return False
    # hair cl
    check_key = 'hcl'
    if not valid_hair(pp[check_key]):
        return False
    # eye cl
    check_key = 'ecl'
    if not valid_eye(pp[check_key]):
        return False
    # pid
    check_key = 'pid'
    if not valid_pid(pp[check_key]):
        return False

    return True

def count_valid(lines):
    valids = 0
    passports = []
    start=0
    for i in range(len(lines)):
        fields = []
        if lines[i] == '\n':
            fields = handle_ppin( lines[start:i], i ) 
            pp = validate_fields( fields)
            if pp:
                if scrutinize(pp):
                    passports.append(pp)
            start = i+1
    return len(passports)

print("{} of all {} passports are valid!".format(count_valid(lines), passportcount))