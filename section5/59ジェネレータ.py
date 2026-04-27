l = ['Goodmorning', 'Hello', 'Goodnight']

for i in l:
    print(i)
print('----------------------------')

def greeting():
    yield 'Goodmorning'
    for i in range(10):
        # yield i
        print(i)
    yield 'Hello'
    yield 'Goodnight'

# for g in greeting():
#     print(g)

g = greeting()
print(next(g))
print('aaaaaaaaaaaa')
print(next(g))
print('aaaaaaaaaaaa')
print(next(g))
print('aaaaaaaaaaaa')
# print(next(g)) # これ以上はもうないのでエラー
