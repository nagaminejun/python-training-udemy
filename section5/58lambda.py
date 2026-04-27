l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun'] # あえてバラバラ

def change_words(words , func):
    print(words)
    print(func.__name__)
    for word in words:
        print(func(word))
    print('----------------------------')

# def sample_func(word):
#     return word.capitalize()

# def sample_func2(word):
#     return word.lower()

sample_func3 = lambda word: word.capitalize() # これも同じ意味
sample_func4 = lambda word: word.lower() # これも同じ意味

change_words(l, sample_func3)
change_words(l, sample_func4)
