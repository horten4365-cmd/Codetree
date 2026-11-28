n = 8
arr = input().split()
sum_val = 0
for i in range(n):
    sum_val += float(arr[i])
    
avg = sum_val/n
print(f"{avg:.1f}")