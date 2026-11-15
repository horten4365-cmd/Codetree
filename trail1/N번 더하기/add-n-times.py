q = input()
p = q.split()
A = int(p[0])
N = int(p[1])
for _ in range(N):
    A += N
    print(A)