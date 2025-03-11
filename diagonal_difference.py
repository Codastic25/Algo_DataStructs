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

def diagonalDifference(arr):
    # Write your code here
    res1 = 0
    res2 = 0
    for i in range (len(arr)):
        res1 += arr[i][i]
        res2 += arr[i][len(arr)-1-i]
    x = abs(res1-res2)
    return x
            