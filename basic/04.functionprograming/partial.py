import functools

int2 = functools.partial(int,base=2)
# int2 10进制转2进制
b = int2('101')
print(b)


max2 = functools.partial(max, 10)
print(max2(1,2,3))   # max(10,1,2,3)
