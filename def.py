#!/usr/bin/python3

'''
定义一个由自己想要功能的函数，以下是简单的规则：

函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None


Python 定义函数使用 def 关键字，一般格式如下：

def 函数名（参数列表）:
    函数体
默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配起来的

给了函数一个名称，指定了函数里包含的参数，和代码块结构。

这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从 Python 命令提示符执行。

strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。

可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：

不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。

可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。



'''

def hello():
    print("hello world")

hello()

def area(width,height):
    return width * height

def print_welcome(name):
    print("welcome",name)

print_welcome("runoob")

w = 4
h = 5

print('width = ',w,"height = ",h,'area = ',area(w,h))

#定义函数
def printme(str):
    #打印任何传入的字符串
    print(str)
    return

#调用函数
printme("我要调用用户自定义函数")
printme("再次调用同一函数")

def ChangeInt(a):
    a = 10

b = 2
ChangeInt(b)
print(b)

#可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了

#可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1,2,3,4])
    print("函数内取值：",mylist)
    return 

#调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值：",mylist)

'''

以下是调用函数时可使用的正式参数类型：

必需参数
关键字参数
默认参数
不定长参数


必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

调用printme()函数，你必须传入一个参数，不然会出现语法错误：


关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。

使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。



'''

#可写函数说明
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return 

#调用printme函数
#printme()



#可写函数说明
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return 

#调用printme函数
printme(str = "菜鸟教程")

#可写函数说明
def printinfo( name, age ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="runoob" )

#用函数时，如果没有传递参数，则会使用默认参数。

#可写函数说明
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="runoob" )
print ("------------------------")
printinfo( name="runoob" )

#你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数

'''
基本语法如下：

def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]

加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。


还有一种就是参数带两个星号 **基本语法如下：

def functionname([formal_args,] **var_args_dict ):
   "函数_文档字符串"
   function_suite
   return [expression]
加了两个星号 ** 的参数会以字典的形式导入


声明函数时，参数中星号 * 可以单独出现，例如:

def f(a,b,*,c):
    return a+b+c
如果单独出现星号 * 后的参数必须用关键字传入。

def f(a,b,*,c):
...     return a+b+c
... 
>>> f(1,2,3)   # 报错
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() takes 2 positional arguments but 3 were given
>>> f(1,2,c=3) # 正常
6
>>>
'''

#可写函数说明

def printinfo(arg1,*vartuple):
    "打印任何传入的参数"
    print("输出：")
    print(arg1)
    print(vartuple)

#调用printinfo函数
printinfo(70,60,50)   #*vartuple可变长的参数，可以输出多个是一个元组

#如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量

# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return
 
# 调用printinfo 函数
printinfo( 10 )
printinfo( 70, 60, 50 )


#可写函数说明

def printinfo1(arg1,**vardict):
    "打印任何传入的参数"
    print("输出：")
    print(arg1)
    print(vardict)

#调用printinfo1函数
printinfo1(1, a=2,b=3)        #两个**以字典的形式传入


'''
python 使用 lambda 来创建匿名函数。

所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。

lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。


ambda 函数的语法只包含一个语句，如下：

lambda [arg1 [,arg2,.....argn]]:expression


'''

#可写函数说明

sum = lambda arg1, arg2: arg1 + arg2

#调用sum函数
print("相加后的值为：",sum(10,20))
print("相加后的值为：",sum(20,20))

'''
return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None

'''

# 可写函数说明
def sum( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print ("函数内 : ", total)
   return total
 
# 调用sum函数
total = sum( 10, 20 )
print ("函数外 : ", total)

'''
Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。

变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：

L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内置作用域（内置函数所在模块的范围）
以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内置中找。

g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域
内置作用域是通过一个名为 builtin 的标准模块来实现的，但是这个变量名自身并没有放入内置作用域内，所以必须导入这个文件才能够使用它。在Python3.0中，可以使用以下的代码来查看到底预定义了哪些变量:

>>> import builtins
>>> dir(builtins)
Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问，如下代码：

>>> if True:
...  msg = 'I am from Runoob'
... 
>>> msg
'I am from Runoob'
>>> 
实例中 msg 变量定义在 if 语句块中，但外部还是可以访问的。

如果将 msg 定义在函数中，则它就是局部变量，外部不能访问：

>>> def test():
...     msg_inner = 'I am from Runoob'
... 
>>> msg_inner
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'msg_inner' is not defined
>>> 
从报错的信息上看，说明了 msg_inner 未定义，无法使用，因为它是局部变量，只有在函数内可以使用。


定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。

局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。
'''

total = 0 # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2 # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total
 
#调用sum函数
sum( 10, 20 )
print ("函数外是全局变量 : ", total)

#当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了

num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num) 
    num = 123
    print(num)
fun1()
print(num)

#如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了

def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()



'''
a = 10
def test():
    a = a + 1
    print(a)
test()
以上程序执行，报错信息如下：

Traceback (most recent call last):
  File "test.py", line 7, in <module>
    test()
  File "test.py", line 5, in test
    a = a + 1
UnboundLocalError: local variable 'a' referenced before assignment
错误信息为局部作用域引用错误，因为 test 函数中的 a 使用的是局部，未定义，无法修改。

修改 a 为全局变量，通过函数参数传递，可以正常执行输出结果为：

实例(Python 3.0+)
#!/usr/bin/python3
 
a = 10
def test(a):
    a = a + 1
    print(a)
test(a)

'''
