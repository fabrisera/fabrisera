import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(arr):
    #check if the array is valid
    for i in range(len(arr)):
        if arr[i] - i - 1 > 2:
            print('Too chaotic')
            return
    #iterate over the array in reverse order
    i = len(arr) - 1
    count = 0
    while i > 0:
        if arr[i] == i + 1:
            i -= 1
        while arr[i] != i + 1:
            d = i + 1 - arr[i]
            for s in range(d):
                temp = arr[i - s]
                arr[i - s] = arr[i - s - 1]
                arr[i - s - 1] = temp
                count += 1
    print(count)            
    return                 






t = int(input())
for t_itr in range(t):
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    minimumBribes(arr)