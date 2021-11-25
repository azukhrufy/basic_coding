#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    
    for x in s[:].split():
        s = s.replace(x,x.capitalize())
    
    return(s)
        
    # res = s.split()
    # print(res)
    # result = []
    # for i in res:
    #     x = list(i)
    #     x[0] = x[0].upper()
    #     result.append(''.join(x))
    
    # return(' '.join(result))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
