q = input()
p = q.split()
a = int(p[0])
b = int(p[1])
prod = 1
for i in range(1, b+1):
    if i%a==0:
        prod*=i

print(prod)