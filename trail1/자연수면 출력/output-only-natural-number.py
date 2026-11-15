T = input()
t = T.split()
A = int(t[0])
B = int(t[1])
if A > 0:
    for i in range(B):
        print(A, end = "")
if A <= 0:
    print('0')