T = input()
t = T.split()
d = t[0]
e = int(t[1])
if d == 'A':
    for i in range(1, e+1):
        print(i, end = " ")
        i += 1
if d == 'D':
    i = e
    for i in range(0, e):
        print(e, end = " ")
        e += -1