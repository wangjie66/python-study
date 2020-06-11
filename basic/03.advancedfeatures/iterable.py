'''
dic
'''
d = {'a': '1', 'b': '2', 'c': '3'}
for n in d :
    print(n)
for n in d.values():
    print(n)
for k,v in d.items():
    list1 =[k,v]
    print(list1)
    print(''.join(list1))

'''
string
'''
for ch in 'ABCD':
    print(ch)

from collections import Iterable
print(isinstance('abc',Iterable))


for i,value in enumerate(['a','b','c']) :
    print((i,value))

def findMinAndMax(L):
    min,max = 0,0
    if not bool(L) :
       return (None,None)
    elif len(L) ==1 :
       return (L[0],L[0])
    for i,n in enumerate(L):
         if i==0 :
             min = n
             max = n
         else :
             if n<min :
                 min = n
             elif n>max :
                 max = n
    return (min , max)



if findMinAndMax([]) != (None, None):
    print('测试失败1!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!')
else:
    print('测试成功!')


