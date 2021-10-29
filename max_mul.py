min1 = min2 = float('inf')
max1 = max2 = -float('inf')
for _ in range(int(input())):
    n = int(input())
    if n < min1:
        min2, min1 = min1, n
    elif n < min2:
        min2 = n

    if n > max1:
        max2, max1 = max1, n
    elif n > max2:
        max2 = n
print(max(max1 * max2, min1 * min2))
