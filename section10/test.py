# long_word = ""
# print('最初のやつ', id(long_word))
# for word in ['aaa', 'bbb', 'ccc']:
#     long_word += "{}xxxx".format(word)
#     print(id(long_word))
# print(long_word)
# print(id(long_word))

# print('--------------------------')
# long_word2 = []
# print('最初のやつで', id(long_word2))
# for word in ['aaa', 'bbb', 'ccc']:
#     long_word2.append("{}xxxx".format(word))
#     print(id(long_word2))
# new_long_word2 = ''.join(long_word2)
# print(new_long_word2)
# print(id(new_long_word2))

# d = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# if 'key' in d:
#     print('OK')

# if 'value1' in d:
#     print('OK')

# if 'key1' in d.keys():
#     print('むだ')

# if 'value1' in d.values():
#     print('valueの取得')

# print(d.items())

# if any('key' in k for k in d):
#     print('部分一致するキーがあります')


def t():
    # num = []
    for i in range(10):
        # yield i
        print(i)
        # num.append(i)
    # return num


# for i in t():
#     print(i)


t()
