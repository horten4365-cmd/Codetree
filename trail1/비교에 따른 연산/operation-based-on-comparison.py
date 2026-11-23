p = input()
o = p.split()
a = int(o[0])
b = int(o[1])
if a > b:
    print(a*b)
else:
    print(b//a)