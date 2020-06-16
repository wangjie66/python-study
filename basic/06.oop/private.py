class Student(object):
    def __init__(self,name,value):
        self.__name = name
        self.__value = value
    def get_name(self):
        return self.__name
    def get_value(self):
        return self.__value


bar = Student('s',3)
print(bar.get_name())
print(bar.get_value())

'''
有些时候，你会看到以一个下划线开头的实例变量名，
比如_name，这样的实例变量外部是可以访问的，
但是，按照约定俗成的规定，当你看到这样的变量时，
意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”
'''