#!/usr/bin/python3
#coding=utf-8
#实例

#用python实现求笛卡儿积

import itertools

class cartesian(object):
    def __init__(self):
        self._data_list=[]

    def add_data(self,data=[]):      #添加生成笛卡儿积的数据列表
        self._data_list.append(data)

    def build(self):                #计算笛卡儿积
        for item in itertools.product(*self._data_list):
            print(item)

if __name__ == "__main__":
    car = cartesian()
    car.add_data([1,2,3,4])
    car.add_data([5,6,7,8])
    car.add_data([9,10,11,12])
    car.build()

#平方根
import cmath

num = float(input('请输入一个数字：'))
num_sqrt = num ** 0.5
num_sqrt1 = cmath.sqrt(num)
print('%0.3f 的平方根为%0.3f'%(num,num_sqrt))
print('%{0}的平方根为{1:0.3f}+{2:0.3f}'.format(num,num_sqrt1.real,num_sqrt1.imag))


#计算二次方程ax**2 + bx+c = 0

import cmath

a =float(input('输入a:'))
b =float(input('输入b:'))
c =float(input('输入c:'))

#计算
d = (b ** 2) - (4 * a * c)

#两种求解方式
sol1 = (-b-cmath.sqrt(d)) / (2 * a)
sol2 = (-b+cmath.sqrt(d)) / (2 * a)

print('结果为{0}和{1}'.format(sol1,sol2))



#计算三角形的面积
a =float(input('输入三角形第一边长:'))
b =float(input('输入三角形第二边长:'))
c =float(input('输入三角形第三边长:'))

#计算半周长
s = (a + b + c) / 2

#计算面积
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('三角形面积为%0.2f'%area)

