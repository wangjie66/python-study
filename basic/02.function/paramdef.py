def power(x,n=2):
    s=1
    while n>0 :
        n=n-1
        s=s*x
    return s

print(power(2,8))
print(power(2))


def add_end(L=[]):
    L.append('END')
    return L

print(add_end([1,3,4]))
print(add_end([1,3,4]))
# 默认参数不能指向可变参数，基本类型和字符不可变，其余均可变
print(add_end())
print(add_end())


def add_end(L=None):
    if L is None:
       L=['END']
    else:
        L.append('END')
    return L

print(add_end())
print(add_end())


'''
可变参数  *
'''

def calc(num):
    s =1
    for n in num :
        s = s +n*n
    return s

print(calc([1,3,4]))

def calcs(*num) :
    s = 1
    for n in num:
        s = s + n * n
    return s

print(calcs(1,3,4))
print(calcs())

'''
关键字参数 **
'''
def p(name,age,**kw):
    print(name,age,kw)

p('wj',333,city='hf')

'''
命名关键字参数 * 
'''
def p(name,age,*,city):
    print(name, age, city)
p('wj', 333, city='hf')

# 有可变参数不需要*隔离
def p(name, age, *args, city):
    print(name, age, args, city)

p('wj', 333, city='hf')


# 参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(args,kw)
f1(*args,**kw)

