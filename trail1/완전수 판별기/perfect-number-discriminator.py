f = 0
s = 0
H = int(input())
for i in range(1, H+1):
    if H % i == 0:
        s += i
        f = s-H
if f == H:
    print('P')
else:
    print('N')