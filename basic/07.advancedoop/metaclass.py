class s():
    pass
print(type(s))
print(type(s()))

'''
__new__()方法接收到的参数依次是：
当前准备创建的类的对象；
类的名字；
类继承的父类集合；
类的方法集合
args: ('MyList', (<class 'list'>,), {'__module__': '__main__', '__qualname__': 'MyList'})
'''
class ListMetaclass(type):
    # def __new__(cls, name, bases, attrs):
    #     print('cls:', cls)
    #     print('name:', name)
    #     print('bases:',bases)
    #     print('attrs:',attrs)
    #     attrs['add'] = lambda self ,value :self.append(value)
    #     return type.__new__(cls, name, bases, attrs)
    def __new__(cls,*args,**kwargs):
        print('args:',args)
        print('kwargs:',kwargs)
        args[2]['add'] = lambda self ,value :self.append(value)
        return type.__new__(cls,*args,**kwargs)


class MyList(list, metaclass=ListMetaclass):
    pass

L =MyList()
L.add(1)
print(L)
