O = input()
B = O.split()
N = int(B[0])
M = int(B[1])
for i in range(N):
    for j in range(M):
        print('*', end = " ")
    print()