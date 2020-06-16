class Student():
     name ="Student"

print(Student.name)
print(Student().name)
a = Student()
a.name="sub"
print(Student.name)
print(Student().name)
print(a.name)



class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count = Student.count+1


# 测试:
if Student.count != 0:
    print('测试失败1!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败2!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败3!')
        else:
            print('Students:', Student.count)
            print('测试通过!')