'''
实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。
实现上下文管理是通过__enter__和__exit__这两个方法实现的
'''


class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)

with Query('Bob') as q:
    q.query()


'''
这两个操作用contextlib代替
'''
from contextlib import contextmanager
class Query1(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query1(name)
    yield q
    print('End')

# 单个语句不打印
# create_query('contextlib')
with create_query('contextlib') as q:
    q.query()

'''
类似aop的操作了。类似decoder
'''
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")

