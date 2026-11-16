P = input()
p = P.split()
N = int(p[0])
a = int(p[1])
i = 1
while i <= N:
    if i % a == 0:
        print(1)
    else:
        print(0)
    i += 1