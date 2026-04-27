animal = 'cat'

def f():
    # global animal
    animal = 'dog'
    print('local:', animal)
    print(locals())

f()
print('global:', animal)
# print(globals())
print(__name__)
