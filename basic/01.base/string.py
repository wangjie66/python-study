#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(b'ABC')
print('中文'.encode('utf-8'))
print(len('ABC'))
print(len('中午'))
print(len(b'ABC'))
print(len('中午'.encode('utf-8')))

print('hello,%s,%s' % ('wj','this is a test.') )
print('%d%%'% (23))

import os
print(os.path)