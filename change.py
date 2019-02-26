#!/usr/loca/bin/python3

'''
int() 函数用于将一个字符串或数字转换为整型。
语法

以下是 int() 方法的语法:

class int(x, base=10)

参数

    x -- 字符串或数字。
    base -- 进制数，默认十进制。


返回值

返回整型数据。

描述

float() 函数用于将整数和字符串转换成浮点数。
语法

float()方法语法：

class float([x])

参数

    x -- 整数或字符串

返回值

返回浮点数。

complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。。
语法

complex 语法：

class complex([real[, imag]])

参数说明：

    real -- int, long, float或字符串；
    imag -- int, long, float；

返回值

返回一个复数。

实例

以下实例展示了 complex 的使用方法：
>>>complex(1, 2)
(1 + 2j)
 
>>> complex(1)    # 数字
(1 + 0j)
 
>>> complex("1")  # 当做字符串处理
(1 + 0j)
 
# 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
>>> complex("1+2j")
(1 + 2j)


str() 函数将对象转化为适于人阅读的形式。
语法

以下是 str() 方法的语法:

class str(object='')

参数

    object -- 对象。

返回值

返回一个对象的string格式。

repr() 函数将对象转化为供解释器读取的形式。
语法

以下是 repr() 方法的语法:

repr(object)

参数

    object -- 对象。

返回值

返回一个对象的 string 格式。

eval() 函数用来执行一个字符串表达式，并返回表达式的值。
语法

以下是 eval() 方法的语法:

eval(expression[, globals[, locals]])

参数

    expression -- 表达式。
    globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
    locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。

返回值

返回表达式计算结果。

tuple 函数将列表转换为元组。。

语法

以下是 tuple 的语法:

tuple( seq )

参数

    seq -- 要转换为元组的序列。

返回值

返回元组。

list() 方法用于将元组或字符串转换为列表。

注：元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。
语法

list()方法语法：

list( seq )

参数

    seq -- 要转换为列表的元组或字符串。

返回值

返回列表。

set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
语法

set 语法：

class set([iterable])

参数说明：

    iterable -- 可迭代对象对象；

返回值

返回新的集合对象

dict() 函数用于创建一个字典。
语法

dict 语法：

class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)

参数说明：

    **kwargs -- 关键字
    mapping -- 元素的容器。
    iterable -- 可迭代对象。

返回值

返回一个字典。

利用 dict(([key,value],[key,value])) 的方式创建字典：

>>> dict((['a',2],['b',3]))
{'a': 2, 'b': 3}

frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
语法

frozenset() 函数语法：

class frozenset([iterable])

参数

    iterable -- 可迭代的对象，比如列表、字典、元组等等。

返回值

返回新的 frozenset 对象，如果不提供任何参数，默认会生成空集合。

chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
语法

以下是 chr() 方法的语法:

chr(i)

参数

    i -- 可以是10进制也可以是16进制的形式的数字。

返回值

返回值是当前整数对应的ascii字符。

ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。
语法

以下是 ord() 方法的语法:

ord(c)

参数

    c -- 字符。

返回值

返回值是对应的十进制整数。

hex() 函数用于将10进制整数转换成16进制，以字符串形式表示。
语法

hex 语法：

hex(x)

参数说明：

    x -- 10进制整数

返回值

返回16进制数，以字符串形式表示。

oct() 函数将一个整数转换成8进制字符串。
语法

oct 语法：

oct(x)

参数说明：

    x -- 整数。

返回值

返回8进制字符串。



'''