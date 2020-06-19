L = [x * x for x in range(10)]
g = (x * x for x in range(10))
for n in g :
    print(n)


def triangles():
    p = [1]
    while True:
        yield p  #generator函数与普通函数的差别：在执行过程中，遇到yield就中断，下次又继续执行
        p = [1] + [p[i] + p[i+1] for i in range(len(p)-1)] + [1]

a = triangles();
print(next(a))
print(next(a))
print(next(a))
print(next(a))
#
# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10.process:
#         break