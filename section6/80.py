import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    @abc.abstractmethod
    def drive(self):
        pass

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError
        
    def drive(self):
        print('Babyは運転できません')

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError
        
    def drive(self):
        print('Adultは運転OKです')

baby = Baby()
adult = Adult()

class Car(object):
    def __init__(self, 
                 model=None):
        self.model = model
        print(model)
    
    def run(self):
        print('carクラスでrun!')

    def ride(self, person):
        person.drive()
        

class ToyotaCar(Car):
    # pass

    def run(self):
        print('ToyotaCarでオーバーライドしたrun')


class TesraCar(Car):
    def __init__(self, password='123',model='Model S', enable_auto_run=False):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run
        self.password = password

    @property
    def enable_auto_run(self):
        return self._enable_auto_run
    
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.password == '123':
            self.enable_auto_run = is_enable
        else:
            print('passwordが違うため不可')

    def auto_run(self):
        print('auto_runです')

car = Car()
car.run()

car.ride(baby)
car.ride(adult)
# car.auto_run()

# toyota_car = ToyotaCar()
# toyota_car.run()

# tesra_car = TesraCar(password='456')
# tesra_car.auto_run()
# tesra_car._enable_auto_run
# tesra_car.enable_auto_run = True
