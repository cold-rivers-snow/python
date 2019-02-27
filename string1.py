#!/usr/bin/python3
#coding=utf-8
#字符串格式输出

print("我叫%s今年%d岁！"%('小明',10))

'''

新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。

基本语法是通过 {} 和 : 来代替以前的 % 。

'''
print("网站名：{name},地址{url}".format(name="菜鸟教程",url="www.runoob.com"))

#通过字典设置参数

site = {"name":"菜鸟教程","url":"www.runoob.com"}
print("网站名：{name},地址{url}".format(**site))

#通过列表索引设置参数
my_list = ['菜鸟教程','www.runoob.com']
print("网站名：{0[0]},地址{0[1]}".format(my_list)) #"0"是必须的


#也可以向 str.format() 传入对象：

class AssignValue(object):
    def __init__(self,value):
        self.value = value
my_value = AssignValue(6)
print('value为:{0.value}'.format(my_value)) #“0“是可选的

print("{}对应的位置是{{0}}".format("runoob"))

para_str = """这是一个多行字符串的实例，多行字符串可以使用制表符
TAB(\t)。
也可以使用换行符[\n]
"""

print (para_str)

'''
capitalize()将字符串的第一个字母变成大写,其他字母变小写。

语法
capitalize()方法语法：

str.capitalize()
参数
无。
返回值
该方法返回一个首字母大写的字符串。

capitalize() 函数补充

需要注意的是：

1、首字符会转换成大写，其余字符会转换成小写。

2、首字符如果是非字母，首字母不会转换成大写，会转换成小写。




'''

str = "this is "
print("str.capitalize()",str.capitalize())

'''
center() 方法返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。

语法
center()方法语法：

str.center(width[, fillchar])
参数
width -- 字符串的总宽度。
fillchar -- 填充字符。
返回值
返回一个指定的宽度 width 居中的字符串，如果 width 小于字符串宽度直接返回字符串，否则使用 fillchar 去填充。

1、如果 width 小于字符串宽度直接返回字符串，不会截断:
2、fillchar 默认是空格
3、fillchar 只能是单个字符
'''

str = "[www.runoob.com]"

print("str.center(40,'*'):",str.center(40,'*'))

list1 = ['google','runoob',1997,2000]
list2 = [1,2,3,4,5,6,7]

print("list1[0]:",list1[0])
print("list2[1:5]",list2[1:5])

print("第三个元素为：",list1[2])
list1[2] = 2001
print("更新后的第三个元素为：",list1[2])


'''
len() 方法返回列表元素个数。

语法
len()方法语法：

len(list)
参数
list -- 要计算元素个数的列表。
返回值
返回列表元素个数。

max() 方法返回列表元素中的最大值。

语法
max()方法语法：

max(list)
参数
list -- 要返回最大值的列表。
返回值
返回列表元素中的最大值。

min() 方法返回列表元素中的最小值。

语法
min()方法语法：

min(list)
参数
list -- 要返回最小值的列表。
返回值
返回列表元素中的最小值。

list() 方法用于将元组或字符串转换为列表。

注：元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。

语法
list()方法语法：

list( seq )
参数
seq -- 要转换为列表的元组或字符串。
返回值
返回列表。

append() 方法用于在列表末尾添加新的对象。

语法
append()方法语法：

list.append(obj)
参数
obj -- 添加到列表末尾的对象。
返回值
该方法无返回值，但是会修改原来的列表。

count() 方法用于统计某个元素在列表中出现的次数。

语法
count()方法语法：

list.count(obj)
参数
obj -- 列表中统计的对象。
返回值
返回元素在列表中出现的次数。

extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。

语法
extend()方法语法：

list.extend(seq)
参数
seq -- 元素列表，可以是列表、元组、集合、字典，若为字典,则仅会将键(key)作为元素依次添加至原列表的末尾。
返回值
该方法没有返回值，但会在已存在的列表中添加新的列表内容。


'''
#语言列表
language = ['French','Englist','German']

#元组
language_tuple = ('Spanish','Portuguese')

#集合
language_set = {'Chinese','Japanese'}

#添加元组元素到列表末尾
language.extend(language_tuple)

print("新列表：",language)

#添加集合元素到列表末尾
language.extend(language_set)

print('新列表：',language)

#del var_name 删除元组列表等变量


'''
元组内置函数
len(tuple)
计算元组元素个数。
max(tuple)
返回元组中元素最大值。

min(tuple)
返回元组中元素最小值。

tuple(seq)
将列表转换为元组。


字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：

d = {key1 : value1, key2 : value2 }
键必须是唯一的，但值则不必。

值可以取任何数据类型，但键必须是不可变的，


'''


#修改字典

dict = {'name':'runoob','age':7,'class':'first'}

dict['age'] = 8
dict['school']= "菜鸟教程"

print("dict['age']",dict['age'])
print("dict['school']",dict['school'])


#能删单一的元素也能清空字典，清空只需一项操作。

del dict['name']        #删除键‘name’

dict.clear()        #清空字典
del dict            #删除字典

#print("dict['age']",dict['age'])
#print("dict['school']",dict['school'])

'''
字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。

两个重要的点需要记住：

1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
字典内置函数：
len(dict)
计算字典元素个数，即键的总数

str(dict)
输出字典，以可打印的字符串表示。

type(variable)
返回输入的变量类型，如果变量是字典就返回字典类型。

clear() 函数用于删除字典内所有元素。

语法
clear()方法语法：

dict.clear()
参数
NA。
返回值
该函数没有任何返回值。

copy() 函数返回一个字典的浅复制。

语法
copy()方法语法：

dict.copy()
参数
NA。
返回值
返回一个字典的浅复制。


'''

#直接赋值和 copy 的区别

dict1 = {'user':'runoob','num':[1,2,3]}

dict2 = dict1   #浅拷贝：引用对象
dict3 = dict1.copy() #浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用

#修改data数据
dict1['user']='root'
dict1['num'].remove(1)

#输出结果
print(dict1)
print(dict2)
print(dict3)

'''

直接赋值：其实就是对象的引用（别名）。

浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。

深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。


b = a: 赋值引用，a 和 b 都指向同一个对象。

b = a.copy(): 浅拷贝, a 和 b 是一个独立的对象，但他们的子对象还是指向统一对象（是引用）。

b = copy.deepcopy(a): 深度拷贝, a 和 b 完全拷贝了父对象及其子对象，两者是完全独立的。


'''

import copy

a = [1,2,3,4,['a','b']]     #原始对象

b = a               #赋值，传对象的引用
c = copy.copy(a)    #对象拷贝，浅拷贝
d = copy.deepcopy(a)#对象拷贝，深拷贝

a.append(5)         #修改对象a
a[4].append('c')    #修改对象a中的['a','b']数组对象

print('a = ',a)
print('b = ',b)
print('c = ',c)
print('d = ',d)
