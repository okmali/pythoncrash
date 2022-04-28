#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    myarr=sorted(arr)
    min=max=0
    
    for num in myarr[:4]:
        min+=num
    
    for num in myarr[1:]:
        max+=num    

    print(min,max)
        
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
