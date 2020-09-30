#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the equalizeArray function below.
def equalizeArray(arr):
    #return len(arr)-max([arr.count(i)for i in arr]) O(n^2) solution
    return len(arr)-max(collections.Counter(arr).values())   #O(n) solution by using import collections 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
