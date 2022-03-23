#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
Example:
s= "12:01:00PM" --> return '12:01:00'
s= "12:01:00AM" --> return '00:01:00'
sample Input: 07:05:45PM'
Sample Output: 19:05:45
"""

def timeConversion(s):
    # Write your code here
    if (s and len(s) == 10):
        am_pm = s[-2:]
        print(am_pm)
        dts = s[0:8].split(':')
        
        hh = int(dts[0])
        mm = int(dts[1])
        ss = int(dts[2])
        
        if(am_pm == "PM"):
            if int(dts[0]) <12:
                hh += 12
        
        if(am_pm == "AM"):
            if int(dts[0]) == 12:
                hh -= 12
        op = "{H:02}:{M:02}:{S:02}"
        return op.format(H=hh,M=mm,S=ss)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()