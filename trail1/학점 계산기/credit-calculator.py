n = int(input())
arr = list(map(float, input().split()))

sum1 = sum(arr)
avg = sum1/n
print(f"{avg:.1f}")    
if avg >= 4.0:
    print('Perfect')
elif avg >= 3.0 and avg < 4.0:
    print('Good')
elif avg < 3.0:
    print('Poor')
