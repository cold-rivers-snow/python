#!/usr/local/bin/python3


#多行注释可以用多个 # 号，
# 还有 ''' 和 """：



'''
第一个注释
第二个注释
'''

"""
第四个注释
第五个注释
"""

print ("hello world!")


#python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。

#缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数

if True:
    print ("True")
else:
    print ("False")

#Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句

total = item_one + \
        item_two + \
        item_three

#在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，
total = ['item_one','item_two','item_three',
        'item_four','item_five']
#python中数字有四种类型：整数、布尔型、浮点数和复数。

'''

    int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
    bool (布尔), 如 True。
    float (浮点数), 如 1.23、3E-2
    complex (复数), 如 1 + 2j、 1.1 + 2.2j

'''



