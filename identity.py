#!/usr/bin/python3
#id() 函数用于获取对象内存地址。
'''
is 与 == 区别：

is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
'''
a = 20
b = 20

if(a is b):
    print("1 - a和b有相同的标识")
else:
    print("1 - a和b没有相同的标识")

if(id(a) == id(b)):
    print("2 - a和b有相同的标识")
else:
    print("2 - a和b没有相同的标识")


#修改变量b的值
b = 30
if(a is b):
    print("3 - a和b有相同的标识")
else:
    print("3 - a和b没有相同的标识")

if(a is not b):
    print("4 - a和b没有相同的标识")
else:
    print("4 - a和b有相同的标识")