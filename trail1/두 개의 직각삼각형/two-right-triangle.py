N = int(input())

for i in range(1, N + 1):
    left_stars = '*' * (N - i + 1)
    spaces = ' ' * (2 * (i - 1))
    right_stars = '*' * (N - i + 1)
    print(left_stars + spaces + right_stars)