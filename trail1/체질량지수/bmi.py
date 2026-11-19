l = input()
k = l.split()
h = int(k[0])
w = int(k[1])
b = (10000*w)//(h**2)
print(f"{b}")
if b > 25:
    print('Obesity')