s1 = list(map(int, input().split()))
s2 = []
for i in s1:
    if i == 0:
        break
    s2.append(i)
for j in s2[::-1]:
    print(j, end = " ")