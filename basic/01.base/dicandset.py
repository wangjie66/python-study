dic = {'a':23 ,'b':12,'c':87}

for i in dic :
    print(i,dic[i])


print(dic)
print(dic['a'])
print(dic.get('b'))
print(dic.get('d','d'))

'''
set
'''
set = set([1,3,4])
print(set)
set.add(3)
print(set)
set.remove(1)
print(set)