N = int(input())

for i in range(1, N+1):
    if i % 2 == 0 or (i % 9 != 0 and i % 3 == 0) or (i % 5 == 0 and i % 10 != 0):
        continue
    print(i, end = " ")
        