s = """\
AAA
BBB
CCC
DDD
"""

# with open('test.txt', 'w+') as f:
#     # f = open('test.txt', 'w')
#     # print('filenikakikomi', file=f)
#     # print('my','name','is','Mike', end='.',file=f)
#     f.write(s)
#     f.seek(0)
#     print(f.read())

with open('test.txt', 'r+') as f:
    print(f.read())
    f.seek(0)
    f.write(s)

# with open('test.txt', 'r') as f:
    # print(f.read())
    # while True:
    #     chunk = 2
    #     # line = f.readline()
    #     line = f.read(chunk)
    #     print(line)
    #     if not line:
    #         break
    # print(f.tell())
    # print(f.read(1))
    # f.seek(3)
    # print(f.read(1))
    # f.seek(4)
    # print(f.read(1))
    # f.seek(5)
    # print(f.read(1))
    # f.seek(6)
    # print(f.read(1))
    # f.seek(7)
    # print(f.read(1))
    # f.seek(8)
    # print(f.read(1))
