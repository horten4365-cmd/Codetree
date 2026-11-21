q = input()
p = q.split()
a = int(p[0])
b = int(p[1])
prod = 1
for i in range(a, b + 1):
    prod *= i

print(prod)
