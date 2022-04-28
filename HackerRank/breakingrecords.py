#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    minRec=maxRec=0
    min=max=scores[0]
    
    for score in scores[1:]:
        if score<min:
            minRec+=1
            min=score
        elif score>max:
            maxRec+=1
            max=score    

    return[maxRec,minRec]

if __name__ == '__main__':
    fptr = open('./myoutput.txt', 'a')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
