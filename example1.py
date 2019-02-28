#!/usr/bin/python3

#生成0-9之间的随机数
#导入random模块

import random

print(random.randint(0,9)) #该函数的语法为：random.randint(a,b)

#变量交换
#1
temp = x
x = y
y = temp

#2
x, y = y, x

#3
x = x + y
y = x - y
x = x - y

#4
x = x ^ y
y = x ^ y
x = x ^ y

#if语句
num = 0
if num > 0:
    print('正数')
elif num == 0:
    print("零")
else:
    print("负数")

if num >= 0:
    if num == 0:
        print("零")
    else:
        print("正数")
else:
    print("负数")

    