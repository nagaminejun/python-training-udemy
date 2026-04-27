class Person(object):
    
    kind = 'human'

    def __init__(self):
        self.x = 100

    # def what_is_your_kind(self):
    #     return self.kind

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

a = Person()
print(a.kind)
print(a.x)
print(a.what_is_your_kind(), 'what_is_your_kind()で呼び出し')
b = Person
print(b.kind)
# print(b.x) # エラー
print(b.what_is_your_kind(), 'classmethodで呼び出した') # エラー


