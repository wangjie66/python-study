#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'the use of module'

__author__ = 'wangjie'

import sys

def test():
    args = sys.argv
    print(args)
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

print(__name__)

if __name__=='__main__':
    test()


'''
类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，
是因为Python并没有一种方法可以完全限制访问private函数或变量，
但是，从编程习惯上不应该引用private函数或变量。
'''