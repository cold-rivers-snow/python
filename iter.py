#!/usr/bin/python3

'''
迭代器有两个基本的方法：iter() 和 next()。

把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 
Python 的构造函数为 __init__(), 它会在对象初始化的时候执行。

__iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。

__next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。

创建一个返回数字的迭代器，初始值为 1，逐步递增 1

StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。



'''

list=[1,2,3,4]
it = iter(list) #创建迭代器对象
print(next(it)) #输出迭代器的下一个元素
print(next(it))

for x in it:
    print(x,end=',')

import sys

list=[1,2,3,4]
it = iter(list)     #创建迭代器

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
##################################
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

##########################################

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)



'''

使用了 yield 的函数被称为生成器（generator）。

跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。

在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。

调用一个生成器函数，返回的是一个迭代器对象。


'''

import sys

def fibonacci(n):   #生成器函数 - 斐波那契
    a,b,counter = 0, 1, 0
    while True:
        if(counter > n):
            return 
        yield a
        a, b = b, a+b
        counter += 1

f = fibonacci(10)   #f是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f),end='')
    except StopIteration:
        sys.exit()

