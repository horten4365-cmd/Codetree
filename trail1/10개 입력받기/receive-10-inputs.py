s1 = list(map(int, input().split()))
s2 = []
c1 = 0
for i in s1:
    if i == 0:
        break
    s2.append(i)
    c1 += 1
s3 = sum(s2)
avg = s3/c1
print(f"{s3} {avg:.1f}")