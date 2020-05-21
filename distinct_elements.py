def countDistinct(arr, N, K):
    array = []
    for i in range(N + 1 - K):
        tot = K
        used = []
        for p in range(i, i + K - 1):
            if arr[p] not in used:
                c = i + K - 1 - p
                for t in range(c):
                    if arr[p] == arr[p + t + 1]:
                        tot -= 1
                used.append(arr[p])      
        array.append(tot)
    return array

arr = [82, 82, 4, 21, 34, 83, 82, 88, 16, 97, 26, 5, 23, 93, 52, 98, 33, 35, 82, 7, 16, 58, 9, 96, 100, 63, 98, 84]

new = countDistinct(arr, 28, 19)
print(new)