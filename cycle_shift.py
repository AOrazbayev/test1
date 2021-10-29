def cycle_shift(arr, n, m):
    for j in range(m):
        k = arr[0]
        for i in range(n - 1):
            arr[i] = arr[i + 1]
        arr[-1] = k


A = [1, 2, 3]
cycle_shift(A, 3, 8)
print(A)