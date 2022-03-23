#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.
Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.
Example 

There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:
0.400000
0.400000
0.200000

Sample Input
arr = [-4, 3, -9, 0, 4, 1]
Sample Output
0.500000
0.333333
0.166667
"""
def plusMinus(arr):
    # Write your code here
    no_positives = 0
    no_negatives = 0
    no_zeros = 0
    arrLen  = len(arr)
    
    for a in arr:
        if a<0: no_negatives +=1
        elif a>0: no_positives +=1
        else: no_zeros +=1
    
    #op = ["{0:.6f}".format(no_positives/arrLen), "{0:.6f}".format(no_negatives/arrLen), "{0:.6f}".format(no_zeros/arrLen)]
    print("{0:.6f}".format(no_positives/arrLen))
    print("{0:.6f}".format(no_negatives/arrLen))
    print("{0:.6f}".format(no_zeros/arrLen))

if __name__ == '__main__':
    #n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
