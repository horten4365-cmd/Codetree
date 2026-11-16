P = input()
p = P.split()
A = int(p[0])
B = int(p[1])
i = A
while i < B+1:
    if i % 2 == 0:
        print(i, end = " ")
        i += 3
    elif i % 2 != 0:
        print(i, end = " ")
        i *= 2    