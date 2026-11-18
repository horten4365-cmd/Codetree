s = 0
a = 0
N = int(input())
for i in range(N):
    a = int(input())
    s += a
print(s, end = " ")
print(f"{s/N:.1f}")