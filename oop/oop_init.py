class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is {}'.format(self.name))


p = Person('Rivers')
p.say_hi()
