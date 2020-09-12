#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * n
    for row in queries:
        for i in range(row[0], row[1] + 1):
            arr[i - 1] += row[2]
    return (max(arr))

nm = input().split()
n = int(nm[0])
m = int(nm[1])
queries = []
for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))
result = arrayManipulation(n, queries)
fptr.write(str(result) + '\n')
fptr.close()
