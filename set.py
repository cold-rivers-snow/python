#!/usr/bin/python3
#coding=utf-8

'''
集合（set）是一个无序的不重复元素序列。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。



'''

basket = {'apple','orange','apple','pear','orange','banana'}

print(basket)       #演示去重功能

'orange' in basket  #判断元素是否在集合内

#展示两个集合间的运算

a = set('abracadabra')
b = set('alacazam')

a

a-b

a|b

a&b         #a和b中都包含的元素

a^b         #不同时包含于a和b的元素

'''
添加元素
语法格式如下：

s.add( x )
将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。

还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：

s.update( x )
x 可以有多个，用逗号分开。

移除元素
语法格式如下：

s.remove( x )
将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误

此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示：

s.discard( x )
我们也可以设置随机删除集合中的一个元素，语法格式如下：

s.pop() 

计算集合元素个数
语法格式如下：

len(s)
计算集合 s 元素个数。

清空集合
语法格式如下：

s.clear()
清空集合 s。

判断元素是否在集合中存在
语法格式如下：

x in s
判断元素 x 是否在集合 s 中，存在返回 True，不存在返回 False。

add() 方法用于给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作。

语法
add()方法语法：

set.add(elmnt)
参数
elmnt -- 必需，要添加的元素。
返回值
无。


clear() 方法用于移除集合中的所有元素。

语法
clear()方法语法：

set.clear()
参数
无。
返回值
无。

copy() 方法用于拷贝一个集合。

语法
copy() 方法语法：

set.copy()
参数
无。
返回值
无。

difference() 方法用于返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中。

语法
difference() 方法语法：

set.difference(set)
参数
set -- 必需，用于计算差集的集合
返回值
返回一个新的集合。

difference_update() 方法用于移除两个集合中都存在的元素。

difference_update() 方法与 difference() 方法的区别在于 difference() 方法返回一个移除相同元素的新集合，而 difference_update() 方法是直接在原来的集合中移除元素，没有返回值。

语法
difference_update() 方法语法：

set.difference_update(set)
参数
set -- 必需，用于计算差集的集合
返回值
无。

discard() 方法用于移除指定的集合元素。

该方法不同于 remove() 方法，因为 remove() 方法在移除一个不存在的元素时会发生错误，而 discard() 方法不会。

语法
discard() 方法语法：

set.discard(value)
参数
value -- 必需，要移除的元素
返回值
无。

intersection() 方法用于返回两个或更多集合中都包含的元素，即交集。

语法
intersection() 方法语法：

set.intersection(set1, set2 ... etc)
参数
set1 -- 必需，要查找相同元素的集合
set2 -- 可选，其他要查找相同元素的集合，可以多个，多个使用逗号 , 隔开
返回值
返回一个新的集合。

intersection_update() 方法用于获取两个或更多集合中都重叠的元素，即计算交集。

intersection_update() 方法不同于 intersection() 方法，因为 intersection() 方法是返回一个新的集合，而 intersection_update() 方法是在原始的集合上移除不重叠的元素。

语法
intersection_update() 方法语法：

set.intersection_update(set1, set2 ... etc)
参数
set1 -- 必需，要查找相同元素的集合
set2 -- 可选，其他要查找相同元素的集合，可以多个，多个使用逗号 , 隔开
返回值
无。

isdisjoint() 方法用于判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。。

语法
isdisjoint() 方法语法：

set.isdisjoint(set)
参数
set -- 必需，要比较的集合
返回值
返回布尔值，如果不包含返回 True，否则返回 False。

issubset() 方法用于判断集合的所有元素是否都包含在指定集合中，如果是则返回 True，否则返回 False。

语法
issubset() 方法语法：

set.issubset(set)
参数
set -- 必需，要比查找的集合
返回值
返回布尔值，如果都包含返回 True，否则返回 False。

issuperset() 方法用于判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回 True，否则返回 False。

语法
issuperset() 方法语法：

set.issuperset(set)
参数
set -- 必需，要比查找的集合
返回值
返回布尔值，如果都包含返回 True，否则返回 False。

pop() 方法用于随机移除一个元素。

语法
pop() 方法语法：

set.pop()
参数
无
返回值
返回移除的元素。

remove() 方法用于移除集合中的指定元素。

该方法不同于 discard() 方法，因为 remove() 方法在移除一个不存在的元素时会发生错误，而 discard() 方法不会。

语法
remove() 方法语法：

set.remove(item)
参数
item -- 要移除的元素
返回值
返回移除的元素。

symmetric_difference() 方法返回两个集合中不重复的元素集合，即会移除两个集合中都存在的元素。

语法
symmetric_difference() 方法语法：

set.symmetric_difference(set)
参数
set -- 集合
返回值
返回一个新的集合。

symmetric_difference_update() 方法移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。

语法
symmetric_difference_update() 方法语法：

set.symmetric_difference_update(set)
参数
set -- 要检测的集合
返回值
无。

union() 方法返回两个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次。

语法
union() 方法语法：

set.union(set1, set2...)
参数
set1 -- 必需，合并的目标集合
set2 -- 可选，其他要合并的集合，可以多个，多个使用逗号 , 隔开。
返回值
返回一个新集合。

update() 方法用于修改当前集合，可以添加新的元素或集合到当前集合中，如果添加的元素在集合中已存在，则该元素只会出现一次，重复的会忽略。

语法
update() 方法语法：

set.update(set)
参数
set -- 必需，可以是元素或集合
返回值
无。



'''

