#!/usr/local/bin/python3

'''
 Python 提供了 getopt 模块来获取命令行参数。

$ python test.py arg1 arg2 arg3

Python 中也可以所用 sys 的 sys.argv 来获取命令行参数：

    sys.argv 是命令行参数列表。

    len(sys.argv) 是命令行参数个数。

注：sys.argv[0] 表示脚本名。
'''

import sys
print ('参数个数为：',len(sys.argv),'个参数')
print ('参数列表',str(sys.argv))