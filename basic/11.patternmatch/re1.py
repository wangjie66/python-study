s = 'ABC\\-001'
s = r'ABC\-001' #r的好处是不需要写转义符号

import re

print(re.match(r'^\d{3}\-\d{3,8}$','010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$','010 12345')) #不匹配返回None

if re.match(r'^\d{3}\-\d{3,8}$','010 12345'):
    print('match .')

print(list('a b   c'.split(' ')))
print(list('a b   c'.split('\s+')))
print(list(re.split('\s+','a b   c')))
print(list(re.split(r'[\s\,\;]+', 'a,b;; c  d')))

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345333')
if bool(m):
    print(m.groups())
    print(m.group(0))

'''
贪婪
'''
print(re.match(r'^(\d+)(0*)$', '102300').groups())
print(re.match(r'^(\d+?)(0*)$', '102300').groups())  #用？可以解决
print(re.match(r'^(\d+?)(0+)(0)$', '102300').groups()) #用指定的也表示特征
print(re.match(r'^(\d+)(0+)$', '102300').groups())


'''
预编译,后面就不需要再次编译
'''
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())


import base64
s = base64.urlsafe_b64encode(b'YWJjZA==')
s = bytes.decode(s)
s = s.replace('=','')
print(str.encode(s))



