#computes the volume given two indices and an array arr returns the volume of the pool
def volume (a, b, arr):
    if arr[b] > arr[a]:
        height = arr[a]
    elif arr[b] == arr[a]:
        height = 0    
    else:
        height = arr[b] 
    volume = height * (b - a - 1)    
    for index in range(b - a - 1):
        if arr[a + 1 + index] <= height:
            volume -= arr[a + 1 + index]
        else:
            volume -= height    
    return volume    

#finds the pools, it must be a recursive function, takes an array and returns an array of arrays of pairs of indices of pools
#pool is an array of arrays
poll = []
def pools(arr):
    if len(arr) < 2:
        haha = True       
    else:    
        #temp is the sorted arr in reverse
        temp = sorted(arr, reverse= True)
        #tallest column
        if temp[0] == temp[1]:
            left = arr.index(temp[0])
            right = arr.index(temp[1], left + 1)
        else:
            left = arr.index(temp[0])
            right = arr.index(temp[1])    
        if left > right:
            tmp = left
            left = right
            right = tmp 
        p = 1     
        while right - left == 1 or right - left == 0:
            left =  arr.index(temp[p])
            p += 1     
        poll.append([big.index(arr[left]), big.index(arr[right])])
        if left != 0:
            pools(arr[0:left + 1])
        if right != len(arr) - 1:
            pools(arr[right:len(arr) + 1])    


#number of test cases
tst = int(input())
#iterating over test cases
for i in range(tst):
    poll = []
    #size of the array
    size = int(input())
    #heights of the columns
    arr = list(map(int, input().split()))
    big = arr
    final = 0
    if len(arr) == 1 or len(arr) == 0:
        print(0)
    else:    
        pools(arr)
        for i in poll:
            final += volume(i[0], i[1], arr)
        print (final)
        print(poll)