#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    ans=0     #两个列表中间存在的特殊值个数为ans
    for i in range(1, 101):            #从1-100里循坏提取i
         #如果i能被a列表任何数整除，且b列表任何数能被i整除，则i为特殊值，all能判断集合值是否为真（集合里的每一个元素都为真）
        if all(i%x==0 for x in a) and all(x%i==0 for x in b): 
            ans += 1   #找到这个数，则计数+1
    return ans  
    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
