#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
For example, the square matrix arr is shown below:
1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = 1+5+9=15.  The right to left diagonal = 3+5+9 =17. Their absolute difference is |15-17|=2 .
'''
def diagonalDifference(arr):
    # Write your code here
    cnt1 =0
    #d1 = [arr[i][j] for i in range(len(arr)) for j in range(len(arr[i]) ) if i==j]
    arrLength = len(arr)
    d1 = [arr[i][i] for i in range(arrLength)]
    d2 = [arr[i][arrLength-1-i] for i in range(len(arr))]
    
    diff = abs(sum(d1)-sum(d2))
    print(diff)
    return diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()