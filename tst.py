tst = int(input())
for i in range(tst):
    size = int(input())
    arr = list(map(int, input().split()))
    list = []
    temp = []
    p = 0
    while p < size:
        while arr[p] <= arr[p + 1]:
            p += 1
        list.append(p)
        if len(temp) == 2:
            list.append(temp)
            temp = []
        p += 1
for i in list:
    if arr[i[0]] < arr[i[1]]:
        temp = arr[i[0]]
    else:
        temp = arr[i[1]]   
    volume += temp * (i[1] - i[0])
    for q in range((i[1] - i[0]) - 2)     
