import math as math

def w(l): 
    w = ""
    if len(r()) > len(l): 
        exit()
    q = open("l.txt", "w")
    for i in l:
        if i == l[-1]: 
            w += str(i)
        else: 
            w += str(i) + ","
    q.write(w)

def r():
    q = open("l.txt", "r")
    l = q.readline().split(",")
    if l == ['']:
        l = [2]
        return l
    a = 0
    for i in l:
        l[a] = int(l[a])
        a += 1
    return l

def p(n, l):
    for i in l: 
        o = n/i
        if int(o) - o == 0 and i <= math.sqrt(n): # from 'and o >= 2' to 'and i <= math.sqrt(n)'
            return False
    return True

def b(n, m, l):
    if n > l[-1]:
        n = l[-1]
    while (n <= m[1]): 
        if p(n, l):
            if n >= m[0] and m[0] != m[1]:
                print(n)
            l.append(n)
        if n == 2:
            n += 1
        else:
            n += 2
    return l

l = [2]
m = [0, 0]
n = m[0]
j = True # l, m and n's dissapointing cousin

l = r()

print("DO NOT INSERT SYMBOLS OTHER THAN NUMBERS") # I'm just lazy
if input("""
1. check number 
2. generate numbers

=> """) == "1":
    e = int(input("insert number => "))
    if e > l[-1]:
        for i in b(l[-1], [e, e], l):
            if i == e:
                print("PRIME")
                j = False
                break
        if (j): 
            print("NOT PRIME")
    else:
        for i in l:
            if i == e:
                print("PRIME")
                j = False
                break
        if (j):
            print("NOT PRIME")
else:
    m[0] = int(input("start number => "))
    m[1] = int(input("end number => "))

n = m[0]

if m[0] > l[-1]:
    l = b(n, m, l) 
else:
    for i in l:
        if i > m[0] and i < m[1]:
            print(i)
    if m[1] > i:
        n = i
        l = b(n, m, l)
w(l)

# there is a weird thing where l.txt always starts with 2, 2, instead of just 2, this doesn't affect performance