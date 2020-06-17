class Animal():
    pass

class Bird(Animal):
    pass

class Parrot(Bird):
    pass

class Run():
    pass

class Parrot2(Bird,Run):
    pass



'''
关于MixIn的命名
'''
class RunMixIn():
    pass


'''
多继承在java中不存在
但python的这种形式，在java中通过多实现接口来实现的
'''

