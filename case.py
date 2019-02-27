#!/usr/bin/python3

#Fibonacci series:菲波那切数列

#两个元素的总和确定了下一个数
#关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
a, b = 0, 1
while b < 1000:
    print(b,end=',')
    a, b = b, a+b
print('\n')

'''
Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。

注意：

1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
3、在Python中没有switch – case语句。

在嵌套 if 语句中，可以把 if...elif...else 结构放在另外一个 if...elif...else 结构中。

if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句

Python中while语句的一般形式：

while 判断条件：
    语句

在 while … else 在条件语句为 false 时执行 else 的语句块

类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中，

'''

n = 100

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d之和为：%d"%(n,sum))
#######################################
count = 0

while count < 5:
    print(count,"小于5")
    count = count + 1
else:
    print(count,"大于或等于5")

#########################################

flag = 0

while(flag):print('欢迎访问菜鸟教程！')
print("Good Bye!")

'''
 for循环可以遍历任何序列的项目，如一个列表或者一个字符串。

for循环的一般格式如下：

for <variable> in <sequence>:
    <statements>
else:
    <statements>

    break 语句用于跳出当前循环体

    如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列

'''

languages = ["c","c++","python","go","shell"]

for x in languages:
    print(x)

############################33

for i in range(4):
    print(i)

#指定区间
for i in range(5,9):
    print(i)

#也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):

for i in range(0,9,3):
    print(i)

#您可以结合range()和len()函数以遍历一个序列的索引

for i in range(len(languages)):
    print(i,languages[i])

'''

Python pass是空语句，是为了保持程序结构的完整性。

pass 不做任何事情，一般用做占位语句，如下实例

python中的True和False


while True:
    pass #等待键盘中断

'''


if 'Hello':
    print("Hello")