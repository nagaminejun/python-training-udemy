class Person(object):
    def __init__(self, name='DefaultName'):
        print(name)
        self.name = name
        print(self.name, ' がinitで実行！')
        self.say_something()
        print(self.name, 'が', self.say_something(), 'と言いました')

    def say_something(self):
        # print('hi!')
        return 'hi!!'

person = Person('Tanaka')
# person.say_something()

person2 = Person()
