sum_val = 0
cnt = 0

for _ in range(10):
    a = int(input())
    if a >= 0 and 200 >= a:
        sum_val += a
        cnt += 1         

avg = sum_val/cnt

# 출력
print(f"{sum_val} {(avg):.1f}")
