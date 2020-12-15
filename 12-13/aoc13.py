from math import floor
from functools import reduce


f = open("input", "r")

lines = [l.strip() for l in f.readlines()]

f.close()


def format_input(lines, kick_x=True):
    eta = int( lines[0] )
    busses = []
    for val in lines[1].split(','):
        if val != 'x' and kick_x:
            busses.append(int(val))
        elif val =='x' and not kick_x:
            busses.append(val)
        elif not kick_x:
            busses.append(int(val))
    return eta, busses


def get_first_line(eta, busses):
    times = [busses[i]*floor(eta/busses[i]) for i in range(0,len(busses))]
    wait_times = [t+busses[i] - eta for i,t in enumerate(times)]
    min_wait_time = min(wait_times)
    index = wait_times.index(min(wait_times))
    return busses[index], wait_times[index]


def get_control_product(eta, busses):
    bid, t = get_first_line(eta, busses)
    return bid*t


def transform_input(lines):
    _, buslines = format_input(lines, kick_x=False)
    lines_with_timestamp = []
    for i, bl in enumerate(buslines):
        if bl != 'x':
            lines_with_timestamp.append( (i, bl) )
    return lines_with_timestamp


def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac


def extended_euclid(m, M):
	if m == 0:
		return (M, 0, 1)
	else:
		gcd, x, y = extended_euclid(M % m, m)
		return (gcd, y - (M//m) * x, x)


####################################################
# taken from https://rosettacode.org/wiki/Chinese_remainder_theorem
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
####################################################


if __name__ == "__main__":
    eta, buslines = format_input(lines)
    print("PART1 : {}".format(get_control_product(eta, buslines)))
    print("-"*80)
    
    ordered_busses = transform_input(lines) 
    print(chinese_remainder( [bid for _, bid in ordered_busses], [-t for t, _ in ordered_busses])  )