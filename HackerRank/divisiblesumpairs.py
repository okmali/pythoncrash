#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    pairCount=0
    firstIndex=0
    while firstIndex < len(ar):
        secondIndex=0
        while secondIndex < len(ar):
            if (firstIndex != secondIndex)and(firstIndex < secondIndex) and ((ar[firstIndex]+ar[secondIndex])%k==0):
                print("new pair:",ar[firstIndex],ar[secondIndex])
                pairCount +=1
            secondIndex+=1
        firstIndex+=1        
    return pairCount            


if __name__ == '__main__':
    fptr = open('./myoutputs.txt', 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
