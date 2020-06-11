list = [x*x for x in range(1,11)]
print (list)

list = [x*x for x in range(1,11) if x%2==0]
print(list)

list = [m+n for m in('ABC') for n in('abc')]
print(list)

import  os
dirs = [d for d in os.listdir("D:/")]
print(dirs)

L = ['Hello', 'World', 'IBM', 'Apple']
l = [s.lower() for s in L]
print(l)

'''
if ... else 要放在for前面
for后面只能放if，不能放else
'''
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [n.lower() if isinstance(n,str) else n  for n in L1  ]
print(L2)

