n0 = input()
n1 = int(n0[0:2])
n2 = int(n0[2:5])
i = n1
while i >= n2:
    print(i, end = " ")
    i -= 2