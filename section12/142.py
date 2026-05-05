import pickle

class Test(object):

    def __init__(self, name):
        self.name = name

data = {
    'a' : [1, 2, 3],
    'b' : ('test', 'test'),
    'c' : {'key' : 'value'},
    'd' : Test('test')
}

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('data.pickle', 'rb') as f:
    data_loaded = pickle.load(f)
    print(data_loaded['d'].name)
    print(type(data_loaded['a']))
    print(type(data_loaded['b']))
    print(type(data_loaded['c']))
