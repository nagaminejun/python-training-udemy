s = set()

for i in range(10):
    s.add(i)

print(s)

ss = {i for i in range(10)}
if ss.add(9):
    print('True')
else:
    print('False')
print(ss)
