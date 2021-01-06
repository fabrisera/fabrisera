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
    d = 0
    while i >= 0:   
        i = len(arr) - 1 - d
        while arr[i] == i + 1:
            i -= 1
            d += 1
        if i < 0:
            print(count)            
            return               
        while arr[i] != i + 1:
            if arr[i] < arr[i - 1]:
                temp = arr[i]
                arr[i] = arr[i - 1]
                arr[i - 1] = temp
                count += 1
                i -= 1
            else:
                i -= 1   
                 
            






t = int(input())
for t_itr in range(t):
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    minimumBribes(arr)