'''
__str__
'''
class Student():
    def __init__(self,name):
        self._name = name
    def __str__(self):
        return 'Student object (name: %s)' % self._name
    __repr__ = __str__  #repr是解决print打印地址的方法，

print(Student('Michael'))
s = Student('Michael')

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
    # 模拟list的取第几个元素
    def __getitem__(self, n ):
        if isinstance(n ,int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a, b = b, a + b
            return L
    '''
    这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
    '''
    def __getattr__(self, attr):
        if attr == 'score':
            return 99


for n in Fib():
    print(n)

print(Fib()[5])

# list(range(100))[5:10.process]

print(Fib()[:5])
print(Fib()[:10:2])

# 当调用一个不存在的属性的时候
print(Fib().score)

'''
动态调用的特性
'''
class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__

print(Chain().status)
print(Chain().status.user.timeline.list)


'''
__call__
'''

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

a = Student('WJ')
print(callable(a))
print(callable('sd'))

