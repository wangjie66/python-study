'''
type
'''

print(type(123))
print(type('123'))
print(type(None))

print(type(abs))


from extend import Animal as a
# import extend as a
print(type(a))

print(type(123) == int)
print(type(a) == a.__class__)

import types

def fn():
    pass

print(type(fn)==types.FunctionType)
print(type(abs)==types.FunctionType)
print(type(abs)==types.BuiltinMethodType)
print(type(lambda x:y)==types.LambdaType)

'''
isinstance
'''
print(isinstance(a(),a))

from extend import Dog as d
print(isinstance(d(),a))
print(isinstance('aa',str))
print(isinstance([1,3],(list,tuple)))
print(isinstance((1,3),(list,tuple)))
print(isinstance('2',(int,str)))

'''
dir
'''
print(dir('abc'))
print(dir(a))
print(dir(11))

print(setattr(a,'a1',33))
print(getattr(a,'a1'))
print(getattr(a,'a2',3))
print(hasattr(a,'a1'))


'''
拓展
'''
# import inspect
# print('abs:',inspect.isfunction(abs))
# print(inspect.isfunction(list))
# print(inspect.ismethod(list))
# print(inspect.isbuiltin(list))