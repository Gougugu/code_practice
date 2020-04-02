#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time = s.split(":")   #时间格式以“：”为间隔切片   切成如下列表【xx， xx， xxxx】
    if s[-2:] == "PM":    #判定是否为下午   s【-2：】是字符串s的倒数两位字符
        if time[0] != "12":     #如果是下午，且不是午夜12点
            time[0] = str(int(time[0])+12)       #小时数+12
    else:
        if time[0] == "12":           #如果是上午，且是上午12点
            time[0] = "00"            #小时数为00
    ntime = ':'.join(time)            #用“：”填充列表间隙
    return str(ntime[:-2])           #以字符串的形式，显示除最后两位以外的结果



if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
