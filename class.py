#!/usr/bin/python3
'''
类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
方法：类中定义的函数。
类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
局部变量：定义在方法中的变量，只作用于当前实例的类。
实例变量：在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
实例化：创建一个类的实例，类的具体对象。
对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

Python中的类提供了面向对象编程的所有基本功能：类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法。

对象可以包含任意数量和类型的数据。


类定义
语法格式如下：

class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>

    类实例化后，可以使用其属性，实际上，创建一个类之后，可以通过类名访问其属性

    类对象
类对象支持两种操作：属性引用和实例化。

属性引用使用和 Python 中所有的属性引用一样的标准语法：obj.name。

类对象创建后，类命名空间中所有的命名都是有效属性名

类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用，像下面这样：

def __init__(self):
    self.data = []


类定义了 __init__() 方法，类的实例化操作会自动调用 __init__() 方法。如下实例化类 MyClass，对应的 __init__() 方法就会被调用:

x = MyClass()
当然， __init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上


self代表类的实例，而非类
类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self

在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。

Python 同样支持类的继承，如果一种语言不支持继承，类就没有什么意义。派生类的定义如下所示:

class DerivedClassName(BaseClassName1):
    <statement-1>
    .
    .
    .
    <statement-N>
需要注意圆括号中基类的顺序，若是基类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找基类中是否包含方法。

BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:

class DerivedClassName(modname.BaseClassName):


Python同样有限的支持多继承形式。多继承的类定义形如下例:

class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。



'''
class MyClass:
    """ 一个简单的类实例"""
    i = 12345
    def f(self):
        return 'hello world'

#实例化类
x = MyClass()

#访问类的属性和方法
print("MyClass 类的属性i为：",x.i)
print("MyClass 类的方法f输出为：",x.f())
################################################3
class Complex:
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0,-4.5)
print(x.r,x.i) #输出结果
#########################################3333
class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()

########################################
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性，私有属性在类外部无法直接访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说：我%d岁"%(self.name,self.age))

#实例化类
p = people('runoob',10,30)
p.speak()


#单继承实例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的析构
        people.__init__(self,n,a,w)
        self.grade = g
    #复写父类的方法
    def speak(self):
        print("%s说：我%d岁了，我在读%d年级"%(self.name,self.age,self.grade))

s = student('ken',10,60,3)
s.speak()

#另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫%s,我是一个演说家，我演讲的主题是%s"%(self.name,self.topic))


#多重继承
class sample(speaker,student):
    a = ''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

test = sample("Tim",25,80,4,"Python")
test.speak()  #方法同名，默认调用的是括号中排前的父类的方法


#如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法，

class Parent:       #定义父类
    def myMethod(self):
        print("调用父类方法")

class Child(Parent):    #定义子类
    def myMethod(self):
        print("调用子类方法")

c = Child()     #子类实例
c.myMethod()    #子类调用重写方法
super(Child,c).myMethod() #用子类对象调用父类已经被覆盖的方法


'''
super() 函数是用于调用父类(超类)的一个方法。

super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。

MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。

语法
以下是 super() 方法的语法:

super(type[, object-or-type])
参数
type -- 类。
object-or-type -- 类，一般是 self

'''

class A:
     def add(self, x):
         y = x+1
         print(y)
class B(A):
    def add(self, x):
        super().add(x)
b = B()
b.add(2)  # 3


class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print ('Parent')
    
    def bar(self,message):
        print ("%s from Parent" % message)
 
class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类B的对象 FooChild 转换为类 FooParent 的对象
        super(FooChild,self).__init__()    
        print ('Child')
        
    def bar(self,message):
        super(FooChild, self).bar(message)
        print ('Child bar fuction')
        print (self.parent)
 
if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')


'''

如果在子类中需要父类的构造方法就需要显式地调用父类的构造方法，或者不重写父类的构造方法。

子类不重写 __init__，实例化子类时，会自动调用父类定义的 __init__。


如果重写了__init__ 时，实例化子类，就不会调用父类已经定义的 __init__
'''

class Father(object):
    def __init__(self,name):
        self.name = name
        print("name:%s"%(self.name))
    def getName(self):
        return 'Father' + self.name

class Son(Father):
    def getName(self):
        return 'Son' + self.name

if __name__ == '__main__':
    son=Son('runoob')
    print(son.getName())



##########################
class Father(object):
    def __init__(self,name):
        self.name = name
        print("name:%s"%(self.name))
    def getName(self):
        return 'Father' + self.name

class Son(Father):
    def __init__(self,name):
        print("hi")
        self.name = name
    def getName(self):
        return 'Son' + self.name

if __name__ == '__main__':
    son=Son('runoob')
    print(son.getName())


'''

如果重写了__init__ 时，要继承父类的构造方法，可以使用 super 关键字：

super(子类，self).__init__(参数1，参数2，....)
还有一种经典写法：

父类名称.__init__(self,参数1，参数2，...)


'''

class Father(object):
    def __init__(self,name):
        self.name = name
        print("name:%s"%(self.name))
    def getName(self):
        return 'Father' + self.name

class Son(Father):
    def __init__(self,name):
        super(Son,self).__init__(name) #Father.__init__(name)
        print("hi")
        self.name = name
    def getName(self):
        return 'Son' + self.name

if __name__ == '__main__':
    son=Son('runoob')
    print(son.getName())

'''
类属性与方法
类的私有属性
__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。

类的方法
在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。

self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定是用 self。

类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。self.__private_methods。

'''

class JustCounter:
    __secretCount = 0   #私有变量
    publicCount = 0     #公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
print(counter.__secretCount) #报错，实例不能访问私有变量


class Site:
    def __init__(self,name,url):
        self.name = name    #public
        self.url = url  #private

    def who(self):
        print("name:",self.name)
        print("url:",self.url)

    def __foo(self):
        print("这是私有方法")

    def foo(self):
        print("这是共有方法")
        self.__foo()

x = Site("菜鸟教程"，'www.runoob.com')
x.who()     #正常输出
x.foo()     #正常输出
x.__foo()   #报错

'''
类的专有方法：
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__truediv__: 除运算
__mod__: 求余运算
__pow__: 乘方


Python同样支持运算符重载，我们可以对类的专有方法进行重载
'''

class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str(self):
        return 'Vector (%d,%d)'%(self.a,self.b)
    
    def __add__(self,other):
        return Vector(self.a + other.a,self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print(v1 + v2)

