#!/usr/bin/python3
#Filename:fibo.py

def fib(n): #定义到n的菲波那切数列
    a,b = 0,1
    while b < n:
        print(b,end=' ')
        a,b = b,a+b 
    print()


def fib2(n): #定义到n的菲波那切数列
    result = []
    a,b = 0,1
    while b < n:
        result.append(b)
        a,b = b,a+b 
    return result


