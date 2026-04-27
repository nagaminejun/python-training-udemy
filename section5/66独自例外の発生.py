class UpperCaseError(Exception):
    pass

# raise IndexError('独自のエラー発生')

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UpperCaseError(word)
        else:
            print('OK!!!')

try:
    check()
except UpperCaseError as exc:
    print('XXXXXXX')
    print(exc)
