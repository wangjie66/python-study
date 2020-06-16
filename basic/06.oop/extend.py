class Animal(object):
    a='2'
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    pass

Dog.run(Dog())
dog = Dog()
dog.run()


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(dog)

'''
静态语言 vs 动态语言
对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
'''

class duck(object):
    def run(self):
        print('duck is running...')

run_twice(duck())