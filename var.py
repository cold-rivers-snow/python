#!/usr/local/bin/python3

counter = 100       #整型变量
miles   = 1000.0    #浮点型变量
name    = "runoob"  #字符串

print(counter)
print(miles)
print(name)


'''
Python3 中有六个标准的数据类型：

    Number（数字）
    String（字符串）
    List（列表）
    Tuple（元组）
    Set（集合）
    Dictionary（字典）

Python3 的六个标准数据类型中：

    不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
    可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。 

    内置的 type() 函数可以用来查询变量所指的对象类型

     a, b, c, d = 20, 5.5, True, 4+3j
>>> print(type(a), type(b), type(c), type(d))
<class 'int'> <class 'float'> <class 'bool'> <class 'complex'>

此外还可以用 isinstance 来判断：
实例
>>>a = 111
>>> isinstance(a, int)
True
>>>


 isinstance 和 type 的区别在于：

    type()不会认为子类是一种父类类型。
    isinstance()会认为子类是一种父类类型。
    del语句删除一些对象引用。

del语句的语法是：

del var1[,var2[,var3[....,varN]]]

可以通过使用del语句删除单个或多个对象。例如：

del var
del var_a, var_b

注意：

    1、Python可以同时为多个变量赋值，如a, b = 1, 2。
    2、一个变量可以通过赋值指向不同类型的对象。
    3、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
    4、在混合计算时，Python会把整型转换成为浮点数。
>>> 2 / 4  # 除法，得到一个浮点数
0.5
>>> 2 // 4 # 除法，得到一个整数
0
>>> 17 % 3 # 取余 
2
>>> 2 ** 5 # 乘方
32

Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。

字符串的截取的语法格式如下：

变量[头下标:尾下标]

Python 没有单独的字符类型，一个字符就是长度为1的字符串。 

Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。

 注意：

    1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
    2、字符串可以用+运算符连接在一起，用*运算符重复。
    3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
    4、Python中的字符串不能改变。

    List（列表） 是 Python 中使用最频繁的数据类型。

列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。

列表是写在方括号 [] 之间、用逗号分隔开的元素列表。

和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。

列表截取的语法格式如下：

变量[头下标:尾下标]

索引值以 0 为开始值，-1 为从末尾的开始位置。

List 内置了有很多方法，例如 append()、pop() 等等，这在后面会讲到。

注意：

    1、List写在方括号之间，元素用逗号隔开。
    2、和字符串一样，list可以被索引和切片。
    3、List可以使用+操作符进行拼接。
    4、List中的元素是可以改变的。


Python 列表截取可以接收第三个参数，参数作用是截取的步长

letters = ['c','h','e','c','k','i','
o']

letters[1:4:2]

['h','c']

元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。

元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取
 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：

tup1 =注意：

    1、与字符串一样，元组的元素不能修改。
    2、元组也可以被索引和切片，方法一样。
    3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
    4、元组也可以使用+操作符进行拼接。注意：

    1、与字符串一样，元组的元素不能修改。
    2、元组也可以被索引和切片，方法一样。
    3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
    4、元组也可以使用+操作符进行拼接。 ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
string、list 和 tuple 都属于 sequence（序列）
注意：

    1、与字符串一样，元组的元素不能修改。
    2、元组也可以被索引和切片，方法一样。
    3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
    4、元组也可以使用+操作符进行拼接。


 集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。

基本功能是进行成员关系测试和删除重复元素。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

创建格式：

parame = {value01,value02,...}
或者
set(value)


 字典（dictionary）是Python中另一个非常有用的内置数据类型。

列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。

键(key)必须使用不可变类型。

在同一个字典中，键(key)必须是唯一的。 


构造函数 dict() 可以直接从键值对序列中构建字典如下：
实例
>>>dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
{'Taobao': 3, 'Runoob': 1, 'Google': 2}
 
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
 
>>> dict(Runoob=1, Google=2, Taobao=3)
{'Runoob': 1, 'Google': 2, 'Taobao': 3}


另外，字典类型也有一些内置的函数，例如clear()、keys()、values()等。

注意：

    1、字典是一种映射类型，它的元素是键值对。
    2、字典的关键字必须为不可变类型，且不能重复。
    3、创建空字典使用 { }。

    
'''

str = 'Runoob'

print (str)     #输出字符串
print (str[0:-1]) #输出第一个到倒数第二个的所有字符
print (str[0])  #输出字符串第一个字符
print (str[2:5])#输出从第三个开始到第五个字符
print (str[2:]) #输出从第三个开始到最后的所有字符
print (str * 2) #输出字符串两次
print (str + "TESt") #连接字符串
print('Ru\noob')
print(r'Ru\noob')


list = ['abcd', 786, 2.23, 'runoob',70.2]
tinylist = [123, 'runoob']

print (list)
print (list[0])
print (list[1:3])
print (list[2:])
print (tinylist * 2)
print (list + tinylist)
 

tuple = ('abcd',786,2.23,'runoob',70.2)
tinytuple = (123,'runoob')

print (tuple)       #输出完整元组
print (tuple[0])    #输出元组的第一个元素
print (tuple[1:3])  #输出从第二个元素开始到第三个元素
print (tuple[2:])   #输出从第三个元素开始的所有元素
print (tinytuple * 2) #输出两次元组
print (tuple + tinytuple) #连接元组


student = {'Tom','Jim','Mary','Tom','Jack','Rose'}

print(student) #输出集合，重复的元素被自动去掉

#成员测试
if 'Rose' in student :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')

#set可以进行集合运算
a = set('abracadabra')
b = set('alaacazam')

print(a)

print(a - b) #a和b的差集
print(a | b) #a和b的并集
print(a & b) #a和b的交集
print(a ^ b) #a和b中不同时存在的元素

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tinydict = {'name':'runoob','code':1,'site':'www.runoob.com'}

print (dict['one']) #输出键为‘one’的值
print (dict[2])     #输出键为2的值
print (tinydict)    #输出完整字典
print (tinydict.keys()) #输出所有键
print (tinydict.values()) #输出所有值

