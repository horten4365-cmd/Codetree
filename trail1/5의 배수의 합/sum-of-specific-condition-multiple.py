# 변수 선언 및 입력
inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
sum_val = 0
if a > b:
    for i in range(b, a + 1):
        if i % 5 == 0:
            sum_val += i
elif b > a:
    for i in range(a, b+1):
        if i % 5 == 0:
            sum_val += i
elif a == b:
    sum_val = a
print(sum_val)