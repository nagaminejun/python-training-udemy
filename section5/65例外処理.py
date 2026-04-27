l = [1,2,3]
i = 5
# del l

try:
    # l[i]
    # () + l
    l[0]
    print('tryが成功した')
except IndexError as ex:
    print("error!!!: {}".format(ex))
except NameError as ne:
    print("error2   : {}".format(ne))
except TypeError as e:
    print("error3   : {}".format(e))
else:
    print('elseが実行された')
finally:
    print('fainlly!!!')
