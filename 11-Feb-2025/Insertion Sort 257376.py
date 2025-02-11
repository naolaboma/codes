# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    tobe = arr[n-1]
    for i in range(n-1,-1,-1):
        if i ==0:
            arr[i] = tobe
            print(" ".join(map(str,arr)))
            break
        if arr[i-1]< tobe:
            arr[i] = tobe
            print(" ".join(map(str,arr)))
            break
        if arr[i-1] > tobe:
            arr[i] = arr[i-1]
        
        print(" ".join(map(str,arr)))          

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
