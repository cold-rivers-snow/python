'''
abs() 函数返回数字的绝对值。

语法
以下是 abs() 方法的语法:

abs( x )
参数
x -- 数值表达式，可以是整数，浮点数，复数。
返回值
函数返回 x（数字）的绝对值，如果参数是一个复数，则返回它的大小。

Python 中 fabs(x) 方法返回 x 的绝对值。虽然类似于 abs() 函数，但是两个函数之间存在以下差异：

abs() 是一个内置函数，而 fabs() 在 math 模块中定义的。
fabs() 函数只适用于 float 和 integer 类型，而 abs() 也适用于复数。

ceil(x) 函数返回一个大于或等于 x 的的最小整数。

语法
以下是 ceil() 方法的语法:

import math

math.ceil( x )
注意：ceil()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。

参数
x -- 数值表达式。
返回值
函数返回返回一个大于或等于 x 的的最小整数。

exp() 方法返回x的指数,ex。

语法
以下是 exp() 方法的语法:

import math

math.exp( x )
注意：exp()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。

参数
x -- 数值表达式。
返回值
返回x的指数,ex。

fabs() 方法返回数字的绝对值，如math.fabs(-10) 返回10.0。

fabs() 函数类似于 abs() 函数，但是他有两点区别:

abs() 是内置函数。 fabs() 函数在 math 模块中定义。

fabs() 函数只对浮点型跟整型数值有效。 abs() 还可以运用在复数中。

语法
以下是 fabs() 方法的语法:

import math

math.fabs( x )
注意：fabs()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。

参数
x -- 数值表达式。
返回值
返回数字的绝对值。

floor(x) 返回数字的下舍整数，小于或等于 x。

语法
以下是 floor() 方法的语法:

import math

math.floor( x )
注意：floor()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。

参数
x -- 数值表达式。
返回值
返回小于或等于 x 的整数。

log() 方法返回x的自然对数，x > 0。

语法
以下是 log() 方法的语法:

import math

math.log( x )
注意：log()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。

参数
x -- 数值表达式。
返回值
返回x的自然对数，x>0。

log10() 方法返回以10为基数的x对数，x>0。

语法
以下是 log10() 方法的语法:

import math

math.log10( x )
注意：log10()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。

参数
x -- 数值表达式。
返回值
返回以10为基数的x对数，x>0。

max() 方法返回给定参数的最大值，参数可以为序列。

语法
以下是 max() 方法的语法:

max( x, y, z, .... )
参数
x -- 数值表达式。
y -- 数值表达式。
z -- 数值表达式。
返回值
返回给定参数的最大值。

min() 方法返回给定参数的最小值，参数可以为序列。

语法
以下是 min() 方法的语法:

min( x, y, z, .... )
参数
x -- 数值表达式。
y -- 数值表达式。
z -- 数值表达式。
返回值
返回给定参数的最小值。

modf() 方法返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。

语法
以下是 modf() 方法的语法:

import math

math.modf( x )
注意：modf()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。

参数
x -- 数值表达式。
返回值
返回x的整数部分与小数部分，

pow() 方法返回 xy（x的y次方） 的值。

语法
以下是 math 模块 pow() 方法的语法:

import math

math.pow( x, y )
内置的 pow() 方法

pow(x, y[, z])
函数是计算x的y次方，如果z在存在，则再对结果进行取模，其结果等效于pow(x,y) %z

注意：pow() 通过内置的方法直接调用，内置方法会把参数作为整型，而 math 模块则会把参数转换为 float。

参数
x -- 数值表达式。
y -- 数值表达式。
z -- 数值表达式。
返回值
返回 xy（x的y次方） 的值。

round() 方法返回浮点数x的四舍五入值。

语法
以下是 round() 方法的语法:

round( x [, n]  )
参数
x -- 数字表达式。
n -- 表示从小数点位数，其中 x 需要四舍五入，默认值为 0。
返回值
返回浮点数x的四舍五入值。

sqrt() 方法返回数字x的平方根。

语法
以下是 sqrt() 方法的语法:

import math

math.sqrt( x )
注意：sqrt()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。

参数
x -- 数值表达式。
返回值
返回数字x的平方根。

choice() 方法返回一个列表，元组或字符串的随机项。

语法
以下是 choice() 方法的语法:

import random

random.choice( seq  )
注意：choice()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。

参数
seq -- 可以是一个列表，元组或字符串。
返回值
返回随机项。

randrange() 方法返回指定递增基数集合中的一个随机数，基数缺省值为1。

语法
以下是 randrange() 方法的语法:

import random

random.randrange ([start,] stop [,step])
注意：randrange()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。

参数
start -- 指定范围内的开始值，包含在范围内。
stop -- 指定范围内的结束值，不包含在范围内。
step -- 指定递增基数。
返回值
从给定的范围返回随机项。

random() 方法返回随机生成的一个实数，它在[0,1)范围内。

语法
以下是 random() 方法的语法:

import random

random.random()
注意：random()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。

参数
无
返回值
返回随机生成的一个实数，它在[0,1)范围内。

seed() 方法改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数。。

语法
以下是 seed() 方法的语法:

import random

random.seed ( [x] )
注意：seed()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。

参数
x -- 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
返回值
本函数没有返回值。

shuffle() 方法将序列的所有元素随机排序。

语法
以下是 shuffle() 方法的语法:

import random
 
random.shuffle (lst )
注意：shuffle()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。

参数
lst -- 列表。
返回值
返回 None。

uniform() 方法将随机生成下一个实数，它在[x,y]范围内。

语法
以下是 uniform() 方法的语法:

import random

random.uniform(x, y)
注意：uniform()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。

参数
x -- 随机数的最小值。
y -- 随机数的最大值。
返回值
返回一个浮点数。

cos() 返回x的反余弦弧度值。

语法
以下是 acos() 方法的语法:

import math

math.acos(x)
注意：acos()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。

参数
x -- -1到1之间的数值。如果x是大于1，会产生一个错误。
返回值
返回x的反余弦弧度值。

asin() 返回x的反正弦弧度值。

语法
以下是 asin() 方法的语法:

import math

math.asin(x)
注意：asin()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。

参数
x -- -1到1之间的数值。如果x是大于1，会产生一个错误。
返回值
返回x的反正弦弧度值。

atan() 返回x的反正切弧度值。

语法
以下是 atan() 方法的语法:

import math

math.atan(x)
注意：atan()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。

参数
x -- 一个数值。
返回值
返回x的反正切弧度值。

atan2() 返回给定的 X 及 Y 坐标值的反正切值。

语法
以下是 atan2() 方法的语法:

import math

math.atan2(y, x)
注意：atan2()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。

参数
x -- 一个数值。
y -- 一个数值。
返回值
返回给定的 X 及 Y 坐标值的反正切值

cos() 返回x的弧度的余弦值。

语法
以下是 cos() 方法的语法:

import math

math.cos(x)
注意：cos()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。

参数
x -- 一个数值。
返回值
返回x的弧度的余弦值,-1 到 1 之间。
hypot() 返回欧几里德范数 sqrt(x*x + y*y)。

语法
以下是 hypot() 方法的语法:

import math

math.hypot(x, y)
注意：hypot()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。

参数
x -- 一个数值。
y -- 一个数值。
返回值
返回欧几里德范数 sqrt(x*x + y*y)。

sin() 返回的x弧度的正弦值。

语法
以下是 sin() 方法的语法:

import math

math.sin(x)
注意：sin()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。

参数
x -- 一个数值。
返回值
返回的x弧度的正弦值，数值在 -1 到 1 之间。

tan() 返回 x 弧度的正切值。

语法
以下是 tan() 方法的语法:

import math

math.tan(x)
注意：tan()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。

参数
x -- 一个数值。
返回值
返回 x 弧度的正切值，数值在 -1 到 1 之间。

degrees() 将弧度转换为角度。

语法
以下是 degrees() 方法的语法:

import math

math.degrees(x)
注意：degrees()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。

参数
x -- 一个数值。
返回值
返回一个角度值。

radians() 方法将角度转换为弧度。

语法
以下是 radians() 方法的语法:

import math

math.radians(x)
注意：radians()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。

参数
x -- 一个数值。
返回值
返回一个角度的弧度值。

pi	数学常量 pi（圆周率，一般以π来表示）
e	数学常量 e，e即自然常数（自然常数）。
'''