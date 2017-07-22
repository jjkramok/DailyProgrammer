import math
import sys

"""   
def my_square_root(n, p, r):
    r = 0
    sqr = n / (10**2)
    ds = [i**2 for i in range(1, 10)]
    best_i = 1
    best_i_delta = math.abs(1 - sqr)
    #Calculate base of square power that is closest to sqr
    for i in ds:
        if i - sqr > -1:
            if i - sqr < best_i_delta:
                best_i = i;
                best_i_delta = i - sqr
    r = best_i # first digit of solution
    n = n - (best_i**2 * 100) #100 is offset, should be calculated dynamically (100 is only for 4 digits first iteration
    best_i = 1
    best_i_delta = math.abs(1 - sqr)
    for j in range(1, 10): #assumes i=9 as max number!
        if ((20*best_i**2 + j)*j) < best_i_delta:
            best_i = i;
            """
def closest_fitting(n):
    """Given a two digit number returns closest base 2 digit that fits in the n"""
    lst = [i**2 for i in range(1, 10) if n-i**2 > -1]
    print(*lst, sep=', ')
    return len(lst)

##Read first integer (precision) from stdin
p = 0;
while True:
    c = sys.stdin.read(1) #reads 1 char in sdtin
    if str.isspace(c):
        break
    p = p * 10 + int(c)

##Read first float (base number) from stdin
f = ""
r = ""
while True:
    c = sys.stdin.read(1) #reads 1 char in sdtin
    #print("char: {0}\n".format(c))
    if str.isspace(c):
        break
    f = f + c
decimals = len(f.split('.')[1]) #splits float into two parts, then calculates length of decimal part
print("precision: {0}".format(p))
print("float: {0}; with {1} decimals".format(f, decimals))

def next_digits(f, r, d, depth=0):
    """Calculates next sqrt digit and adds it to r, for number f. d are the amount of decimals given on input"""
    lst = [20*r*b + b**2 for b in range(1, 10) if float(f) - (20*r*b + b**2) > -1]
    print(*lst, sep=', ')
    r += str(len(lst))
    f = str(round(float(f) - float(lst[-1:][0]), d))
    print("After Part B1, float: {0}; res: {1}".format(f, r))
    depth += 1
    return (f, r, depth)

## (10A)**2 + 2(10AB) + B**2
## 10**2 * A**2 <= f
## 2(10AB) + B**2 => (20A + B)*B
#Start with part A of the approx.
a_sqrt = f[0:2] #splice first two chars from the float
closest_base = closest_fitting(int(a_sqrt))
temp = int(a_sqrt) - closest_base**2
if temp < 10:
    f = "0" + str(temp) + f[2:]
else:
    f = str(temp)+ f[2:]
r += str(closest_base)
print("After Part A, float: {0}; res: {1}".format(f, r))
next_digits(f, r, decimals)
while p > 0:
    break; #remove later
    next_digits()
    p -= 1

    

    
    
    
