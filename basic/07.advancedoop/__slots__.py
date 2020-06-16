class student():
    pass

s1 = student()
s1.name = '333'
s1.abs = abs ;

print(s1.abs(-1))

s2 = student()

print(hasattr(s1,'abs'))
print(hasattr(s2,'abs'))

student.abs =abs ;

print(hasattr(s2,'abs'))


class student2():
    __slots__ = ('name','age')

s3 = student2()
s3.name = 'ddd'
# s3.score = 3
# print(s3.score)

# 对继承类不生效
class substu(student2):
    pass

s4 = substu() ;
s4.score =3
print(s4.score)
