#number of test cases
tst = int(input())
#iterating over test cases
for i in range(tst):
    #size of the array
    size = int(input())
    #heights of the columns
    arr = list(map(int, input().split()))
    #p iterates over the array, direction is a boolean specifying whether we are going up (true) or down (false)
    #we begin by going up, the goal is to divide the array is subarrays 
    sub_arr = []
    temp = []
    direction = True
    while p < size:
        #if we are going up
        if direction:                    
            while arr[p] <= arr[p + 1]:
                p += 1
            temp.append(p)
            direction = False
            if len(temp) == 2:
                sub_arr.append(temp)
                temp = []       
            p += 1
        else:
            while arr[p] >= arr[p + 1]:
                p += 1
            temp.append(p)
            direction = False
            if len(temp) == 2:
                sub_arr.append(temp)
                temp = []       
            p += 1  
#now i am iterating over the sub_arr (or the pools and computing the relative volume)             
for i in sub_arr:
    #chosing the min height
    if arr[i[0]] < arr[i[1]]:
        temp = arr[i[0]]
    else:
        temp = arr[i[1]]  
    #computing the max volume     
    volume += temp * (i[1] - i[0])
    #removing the middle blocks
    for index in range((i[1] - i[0]) - 1):
        arr[i[0] + index]
