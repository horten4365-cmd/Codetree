q = input()
p = q.split()
a = int(p[0])
b = int(p[1])
prod = 1
for i in range(b):
    prod *= a
print(prod)