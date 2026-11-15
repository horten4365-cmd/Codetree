T = input()
t = T.split()
a = int(t[0])
b = int(t[1])
if b >= a:
    for i in range(b, a - 1, -1):
        print(i, end=" ")
else:
    for i in range(a, b - 1, -1):
        print(i, end=" ")