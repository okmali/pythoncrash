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

def lonelyinteger(a):
    # Write your code here
    firstIndex=0
    lonelyInt=a[firstIndex]
    while firstIndex < len(a):
        secondIndex=0
        found=True
        while secondIndex < len(a):
            if (firstIndex != secondIndex) and (a[firstIndex]==a[secondIndex]):
                found=False
                break
            else:
                secondIndex+=1
        
        if found:
            break
        else:
            firstIndex+=1

    print(a[firstIndex])
    return a[firstIndex] 
if __name__ == '__main__':

    fptr = open('./myoutputs.txt', 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
