def now1():
    print("2020-6-11.patternmatch")

name = now1.__name__
print(name)
print(now1.__code__)

def log(fn):
    def wrapper(*args,**kwargs):
        print('call %s():' % fn.__name__)
        return fn(*args,**kwargs)
    return wrapper

@log
def now2():
    print("2020-6-11.patternmatch")

now2()


def logp(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logp("haha")
def now2():
    print("2020-6-11.patternmatch")

now2()
print(now2.__name__)

import functools

def log2(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log2
def now2():
    print("2020-6-11.patternmatch")

now2()
print(now2.__name__)