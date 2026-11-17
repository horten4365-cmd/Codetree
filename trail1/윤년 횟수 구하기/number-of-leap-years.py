N = int(input())
cnt1 = 0
for i in range(1,N+1):
    if i % 4 == 0 and i % 100 != 0 and i != 0:
        cnt1 += 1
    if i % 400 == 0 and i != 0:
        cnt1 += 1
print(cnt1)