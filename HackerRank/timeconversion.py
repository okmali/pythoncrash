#!/bin/python3

import math
import os
import random
import re
import sys
from time import strftime
from time import strptime
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    tm=strptime(s,"%I:%M:%S%p")
    return tm


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open('./myoutputs.txt', 'w')

    s = input()

    #s = "07:05:45PM"
    result = timeConversion(s)

    print (strftime("%H:%M:%S",result))
    fptr.write(strftime("%H:%M:%S",result) + '\n')

    fptr.close()