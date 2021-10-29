def swap(arr, k):
    edge = len(arr) - len(arr) % k
    for i in range(0, edge, 2*k):
        for j in range(i, i+k):
            if j + k < len(arr):
                arr[j], arr[j+k] = arr[j+k], arr[j]


test = [0, 1, 2, 3]
swap(test, 1)
print(test)
