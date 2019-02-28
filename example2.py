#!/usr/bin/python3
#判断字符串是否为数字

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError,ValueError):
        pass
    
    return False

# 测试字符串和数字
print(is_number('foo'))   # False
print(is_number('1'))     # True
print(is_number('1.3'))   # True
print(is_number('-1.37')) # True
print(is_number('1e3'))   # True
 
# 测试 Unicode
# 阿拉伯语 5
print(is_number('٥'))  # True
# 泰语 2
print(is_number('๒'))  # True
# 中文数字
print(is_number('四')) # True
# 版权号
print(is_number('©'))  # False

'''
isdigit() 方法检测字符串是否只由数字组成。

语法
isdigit()方法语法：

str.isdigit()
参数
无。
返回值
如果字符串只包含数字则返回 True 否则返回 False。

'''

str = "123456"; 
print (str.isdigit())

str = "Runoob example....wow!!!"
print (str.isdigit())


'''
isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。

注：定义一个字符串为Unicode，只需要在字符串前添加 'u' 前缀即可，具体可以查看本章节例子。

语法
isnumeric()方法语法：

str.isnumeric()
参数
无。
返回值
如果字符串中只包含数字字符，则返回 True，否则返回 False

'''

str = "runoob2016"  
print (str.isnumeric())

str = "23443434"
print (str.isnumeric())

#判断奇偶数

num = 9
if(num % 2) == 0:
    print("{0}是偶数".format(num))
else:
    print("{0}是奇数".format(num))


#1判断闰年
year = 2019
if(year % 4) == 0:
    if(year % 100) == 0:
        if(year % 400) == 0:
            print("{0}是闰年".format(year))
        else:
            print("{0}不是闰年".format(year))
    else:
        print("{0}是闰年".format(year))
else:
    print("{0}不是闰年".format(year))

#2
if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    print("{0}是闰年".format(year))
else:
    print("{0}不是闰年".format(year))


#3
import calendar

check_year=calendar.isleap(year)
if check_year == True:
    print ("闰年")
else:
    print ("平年")


# 最简单的
print(max(1, 2))
print(max('a', 'b'))
 
# 也可以对列表和元组使用
print(max([1,2]))
print(max((1,2)))
 
# 更多实例
print("80, 100, 1000 最大值为: ", max(80, 100, 1000))
print("-20, 100, 400最大值为: ", max(-20, 100, 400))
print("-80, -20, -10最大值为: ", max(-80, -20, -10))
print("0, 100, -400最大值为:", max(0, 100, -400))

#质数

num = 2
if num > 1:
    for i in range(2,num):
        if(num % i) == 0:
            print(num,"不是质数")
            print(i,"乘于",num//i,"是",num)
            break
    else:
        print(num,"是质数")

else:
    print(num,"不是质数")


lower = 2
upper = 999

for num in range(lower,upper + 1):
    # 素数大于 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)


num = 3
factorial = 1
 
# 查看数字是负数，0 或 正数
if num < 0:
   print("抱歉，负数没有阶乘")
elif num == 0:
   print("0 的阶乘为 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("%d 的阶乘为 %d" %(num,factorial))           


# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()


# Python 斐波那契数列实现
 
# 获取用户输入数据
#nterms = int(input("你需要几项？"))
nterms = 9
 
# 第一和第二项
n1 = 0
n2 = 1
count = 2
 
# 判断输入的值是否合法
if nterms <= 0:
   print("请输入一个正整数。")
elif nterms == 1:
   print("斐波那契数列：")
   print(n1)
else:
   print("斐波那契数列：")
   print(n1,",",n2,end=" , ")
   while count < nterms:
       nth = n1 + n2
       print(nth,end=" , ")
       # 更新值
       n1 = n2
       n2 = nth
       count += 1

'''
# 获取用户输入的数字
num = int(input("请输入一个数字: "))
 
# 初始化变量 sum
sum = 0
# 指数
n = len(str(num))
 
# 检测
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** n
   temp //= 10
 
# 输出结果
if num == sum:
   print(num,"是阿姆斯特朗数")
else:
   print(num,"不是阿姆斯特朗数")


# 获取用户输入数字
lower = int(input("最小值: "))
upper = int(input("最大值: "))
 
for num in range(lower,upper + 1):
   # 初始化 sum
   sum = 0
   # 指数
   n = len(str(num))
 
   # 检测
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** n
       temp //= 10
 
   if num == sum:
       print(num)  



# 用户输入字符
c = input("请输入一个字符: ")
 
# 用户输入ASCII码，并将输入的数字转为整型
a = int(input("请输入一个ASCII码: "))
 
 
print( c + " 的ASCII 码为", ord(c))
print( a , " 对应的字符为", chr(a))
'''


#定义一个函数
def hcf(x,y):
    """该函数返回两个数的最大公约数"""

    #获取最小值
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1,smaller + 1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf


#定义函数
def lcm(x,y):

    #获取最大的数
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

#用户输入两个数字
num1 = int(input("输入第一个数字："))
num2 = int(input("输入第二个数字："))

print(num1,"和",num2,"的最大公约数为：",hcf(num1,num2))
print(num1,"和",num2,"的最小公倍数为：",lcm(num1,num2))



# 定义函数
def add(x, y):
   """相加"""
 
   return x + y
 
def subtract(x, y):
   """相减"""
 
   return x - y
 
def multiply(x, y):
   """相乘"""
 
   return x * y
 
def divide(x, y):
   """相除"""
 
   return x / y
 
# 用户输入
print("选择运算：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")
 
choice = input("输入你的选择(1/2/3/4):")
 
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))
 
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
 
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
 
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
 
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("非法输入")

import calendar

yy = int(input("输入年份："))
mm = int(input("输入月份:"))

print(calendar.month(yy,mm))


def recur_fibo(n):
   """递归函数
   输出斐波那契数列"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
 
 
# 获取用户输入
nterms = int(input("您要输出几项? "))
 
# 检查输入的数字是否正确
if nterms <= 0:
   print("输入正数")
else:
   print("斐波那契数列:")
   for i in range(nterms):
       print(recur_fibo(i))

with open("test.txt","wt") as out_file:
    out_file.write("该文本会写入到文件中\n看到我了吧")

with open("test.txt","rt") as in_file:
    text = in_file.read()

print(text)


'''

w, r, wt, rt 都是 python 里面文件操作的模式。

w 是写模式，r 是读模式。

t 是 windows 平台特有的所谓 text mode(文本模式）,区别在于会自动识别 windows 平台的换行符。

类 Unix 平台的换行符是 \n，而 windows 平台用的是 \r\n 两个 ASCII 字符来表示换行，python 内部采用的是 \n 来表示换行符。

rt 模式下，python 在读取文本时会自动把 \r\n 转换成 \n。

wt 模式下，Python 写文件时会用 \r\n 来表示换行。


'''


# 测试实例一
print("测试实例一")
str = "runoob.com"
print(str.isalnum()) # 判断所有字符都是数字或者字母
print(str.isalpha()) # 判断所有字符都是字母
print(str.isdigit()) # 判断所有字符都是数字
print(str.islower()) # 判断所有字符都是小写
print(str.isupper()) # 判断所有字符都是大写
print(str.istitle()) # 判断所有单词都是首字母大写，像标题
print(str.isspace()) # 判断所有字符都是空白字符、\t、\n、\r

print("------------------------")

# 测试实例二
print("测试实例二")
str = "runoob"
print(str.isalnum()) 
print(str.isalpha()) 
print(str.isdigit()) 
print(str.islower()) 
print(str.isupper()) 
print(str.istitle()) 
print(str.isspace()) 


str = "www.runoob.com"
print(str.upper())          # 把所有字符中的小写字母转换成大写字母
print(str.lower())          # 把所有字符中的大写字母转换成小写字母
print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写 

import calendar

monthRange = calendar.monthrange(2016,9)
print(monthRange)

# 引入 datetime 模块
import datetime
def getYesterday(): 
    today=datetime.date.today() 
    oneday=datetime.timedelta(days=1) 
    yesterday=today-oneday  
    return yesterday
 
# 输出
print(getYesterday())


'''

ist 增加元素
>>> li 
['a', 'b', 'mpilgrim', 'z', 'example']
>>> li.append("new")
>>> li 
['a', 'b', 'mpilgrim', 'z', 'example', 'new']
>>> li.insert(2, "new")
>>> li 
['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new']
>>> li.extend(["two", "elements"]) 
>>> li 
['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']

list 搜索
>>> li 
['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
>>> li.index("example")
5
>>> li.index("new")
2
>>> li.index("c")
Traceback (innermost last):
 File "<interactive input>", line 1, in ?
ValueError: list.index(x): x not in list
>>> "c" in li
False
5.list 删除元素
>>> li 
['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
>>> li.remove("z")  
>>> li 
['a', 'b', 'new', 'mpilgrim', 'example', 'new', 'two', 'elements']
>>> li.remove("new")    # 删除首次出现的一个值
>>> li 
['a', 'b', 'mpilgrim', 'example', 'new', 'two', 'elements']    # 第二个 'new' 未删除
>>> li.remove("c")     #list 中没有找到值, Python 会引发一个异常
Traceback (innermost last): 
 File "<interactive input>", line 1, in ? 
ValueError: list.remove(x): x not in list
>>> li.pop()      # pop 会做两件事: 删除 list 的最后一个元素, 然后返回删除元素的值。
'elements'
>>> li 
['a', 'b', 'mpilgrim', 'example', 'new', 'two']
6.list 运算符
>>> li = ['a', 'b', 'mpilgrim']
>>> li = li + ['example', 'new']
>>> li 
['a', 'b', 'mpilgrim', 'example', 'new']
>>> li += ['two']         
>>> li 
['a', 'b', 'mpilgrim', 'example', 'new', 'two']
>>> li = [1, 2] * 3
>>> li 
[1, 2, 1, 2, 1, 2] 
7.使用join链接list成为字符串
>>> params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
>>> ["%s=%s" % (k, v) for k, v in params.items()]
['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
>>> ";".join(["%s=%s" % (k, v) for k, v in params.items()])
'server=mpilgrim;uid=sa;database=master;pwd=secret'
join 只能用于元素是字符串的 list; 它不进行任何的类型强制转换。连接一个存在一个或多个非字符串元素的 list 将引发一个异常。

8.list 分割字符串
>>> li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
>>> s = ";".join(li)
>>> s 
'server=mpilgrim;uid=sa;database=master;pwd=secret'
>>> s.split(";")   
['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
>>> s.split(";", 1) 
['server=mpilgrim', 'uid=sa;database=master;pwd=secret']
split 与 join 正好相反, 它将一个字符串分割成多元素 list。

注意, 分隔符 (";") 被完全去掉了, 它没有在返回的 list 中的任意元素中出现。

split 接受一个可选的第二个参数, 它是要分割的次数。

9.list 的映射解析
>>> li = [1, 9, 8, 4] 
>>> [elem*2 for elem in li]    
[2, 18, 16, 8] 
>>> li
[1, 9, 8, 4] 
>>> li = [elem*2 for elem in li] 
>>> li 
[2, 18, 16, 8] 
10.dictionary中的解析
>>> params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
>>> params.keys()
['server', 'uid', 'database', 'pwd']
>>> params.values()
['mpilgrim', 'sa', 'master', 'secret']
>>> params.items()
[('server', 'mpilgrim'), ('uid', 'sa'), ('database', 'master'), ('pwd', 'secret')]
>>> [k for k, v in params.items()]
['server', 'uid', 'database', 'pwd']
>>> [v for k, v in params.items()]
['mpilgrim', 'sa', 'master', 'secret']
>>> ["%s=%s" % (k, v) for k, v in params.items()]
['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
11.list 过滤
>>> li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
>>> [elem for elem in li if len(elem) > 1]
['mpilgrim', 'foo']
>>> [elem for elem in li if elem != "b"]
['a', 'mpilgrim', 'foo', 'c', 'd', 'd']
>>> [elem for elem in li if li.count(elem) == 1]
['a', 'mpilgrim', 'foo', 'c']



'''


people={}
for x in range(1,31):
    people[x]=1
# print(people)
check=0
i=1
j=0
while i<=31:
    if i == 31:
        i=1
    elif j == 15:
        break
    else:
        if people[i] == 0:
            i+=1
            continue
        else:
            check+=1
            if check == 9:
                people[i]=0
                check = 0
                print("{}号下船了".format(i))
                j+=1
            else:
                i+=1
                continue