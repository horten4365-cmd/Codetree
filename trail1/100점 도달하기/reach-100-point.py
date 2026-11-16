N = int(input())
while N <= 100:
    if N >= 90:
        print('A', end = " ")
    elif N >= 80 and N < 90:
        print('B', end = " ")
    elif 80 > N and N >= 70:
        print('C', end = " ")
    elif 70 > N and N >= 60:
        print('D', end = " ")
    elif 60 > N:
        print('F', end = " ")
    N += 1