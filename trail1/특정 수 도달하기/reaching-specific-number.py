arr=list(map(int,input().split(" ")))

sarr = 0
cnt = 0
for i in range(10):
    if arr[i] <= 250:
        sarr += arr[i]
        cnt += 1
    elif arr[i] > 250:
        break
avg = sarr / cnt
print(sarr, f"{avg:.1f}")