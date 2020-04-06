#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    orange_count = 0                   # 接到的橙子数
    appel_count = 0                  #接到的苹果树
    for appel in apples:         #遍历 掉下来的苹果
        if (appel + a) >= s and (appel + a) <= t:   #看滚到屋子的苹果
            appel_count +=1            # 喜+1

    for orange in oranges:     #同上
        if (orange + b) >= s and (orange + b)<= t:
            orange_count +=1           

    count = [appel_count, orange_count]          #组合

    for i in count:    #遍历打印
        print(i)

    


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
