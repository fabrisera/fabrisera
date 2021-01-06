#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    temp = []
    pairs = 0
    for i in ar:
        if i in temp:
            pairs += 1
            temp.remove(i)
        else:
            temp.append(i)
    return pairs            



n = int(input())

ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)

print(result)
