N = int(input())
for i in range(N+1):
    for j in range((N)-i):
        print('*'*(N-i), end = " ")
    print()