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
        l[a] = int(l[a]) # l is still str
        a += 1
    return l

def p(n, l):
    for i in l: 
        o = n/i
        if int(o) - o == 0 and o >= 2:
            return False
    return True

def b(n, m, l):
    if n == 2:
        n += 1
    else:
        n += 2
    while (n <= m[1]): 
        if p(n, l):
            if n >= m[0]:
                print(n)
            l.append(n)
        n += 2
    return l

l = [2]
m = [89950, 90000] # insert start and max number, if m[0] is larger than l[-1] then it won't work
n = m[0] # change to m[0] or have it at 3 if it doesn't work

l = r()

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