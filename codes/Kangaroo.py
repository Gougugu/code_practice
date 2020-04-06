#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if x1 > x2 and v1 < v2 and (x1 - x2) % (v2 - v1) == 0:   #  两个一元函数整点相交基本条件， 初始点高者， 变化趋势小。  且 初始差距能被 变化趋势差整除。 
        result = "YES"              
    elif x1 == x2 and v1 == v2:             # 或为相同函数  （重叠）
        result = "YES"
    elif x1 < x2 and v1 > v2 and (x2 - x1) % (v1 - v2) == 0:    #  或初始点 低者， 变化趋势大。
        result = "YES"
    else:    # 不满足以上条件则不会出现交点。
        result = "NO"

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
