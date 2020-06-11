'''
函数本身可以赋值给变量名

'''

f =abs(-10)
print(f)

f=abs
print(f(-10))

def myabs(x,y,f):
    print(f(x)+f(y))

myabs(-5,3,abs)

'''
map/reduce
'''
def f(x):
    return  x*x

a = map(f,range(1,11))
print(map(f,range(1,11)))
print(list(a))
print([a])

from functools  import reduce
def fn(x,y):
    return x*10+y
a = reduce(fn,range(1,6))
print(a)


# 测试
def normalize(name):
    list = []
    r = ''
    for i, m in enumerate(name):
        if i == 0:
            r = r + m.upper()
        else:
            r = r + m.lower()
    list.append(r)
    return list
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce


def prod(L):
    return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')



from functools import reduce
CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)

print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}
def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))


'''
filter
'''
def is_odd(n):
    return  n%2 ==1
print(list(filter(is_odd,[1,2,4,5,6,9])))


def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

'''
sorted 
'''
a =sorted([36, 5, -12, 9, -21], key=abs)
print(a)

a = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(a)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
print(sorted(L,key=by_name))

print(by_name(('bb',34)))