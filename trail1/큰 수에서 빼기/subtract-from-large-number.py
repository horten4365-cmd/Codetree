p = input()
o = p.split()
A = int(o[0])
B = int(o[1])
if A > B:
    print(A-B)
if B > A:
    print(B-A)
if A == B:
    print(0)