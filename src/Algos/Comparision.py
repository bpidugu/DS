#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

'''
Example 
arr = [1,1,3,2,1]
All of the values are in the range [0...3]
Frequency of arra is [0,3,1,1] => sorted = [1,1,1,2,3]
'''
def countingSort(arr):
    # Write your code here
    maxVal = max(arr)
    
    
    rArr = [0]*(maxVal+1)
    
    print(maxVal)
    
    for i in arr:
        rArr[i] +=1
    
    op = []
    #print(rArr)
    for i in range(len(rArr)):
        if(rArr[i]!=0):
            op.append([rArr[i]*i])
    
    #print(rArr[-1])
    #if (rArr[-1]==0): del(rArr[-1])
    
    #if (rArr[0]==0): rArr = rArr[1:]
 
    
    return rArr
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
