#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    retgrade=[]
    for grade in grades:
        if grade<38:
            retgrade.append(grade)
        else:
            remaining=5-(grade%5)
            if (remaining <3):
                retgrade.append(grade+remaining)
            else:    
                retgrade.append(grade)    
    return retgrade

if __name__ == '__main__':
    fptr = open('./myoutputs.txt', 'w')

    grades_count = int(input().strip())

    grades = []

    grades = list(map(int, input().rstrip().split()))

    '''
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    '''
    result = gradingStudents(grades)
    print(result)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
