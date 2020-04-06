#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the knightlOnAChessboard function below.
def knightlOnAChessboard(n):
    







if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
