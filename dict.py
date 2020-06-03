#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    p = 0
    arr = []
    while n > 0:
        while 2 ** p <= n:
            p += 1
        p -= 1    
        arr.append(p)
        n -= 2 ** p
    if len(arr) == 0:
        print(0)    
    else:
        maxi = 1
        for i in range(len(arr) - 1):
            temp = 1
            b = i
            while arr[b] == arr[b + 1]:
                temp += 1
                b += 1
            if temp > maxi:
                maxi = temp
        print(maxi)            




