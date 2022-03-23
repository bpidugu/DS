#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

"""
Given an array of integers, where all elements but one occur twice, find the unique element.
a=[1,2,3,4,3,2,1]
The Unique element is 4

"""
def lonelyinteger(a):
    # Write your code here
    d = {}
    for i in a:
        if( i in d.keys()):
            cnt = d[i]
            cnt +=1
            d[i] = cnt
        else:
            d[i] = 1
    
    op = [l for l in d if d[l]==1]
    return op[0] if len(op) >0 else None

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
