s = 'aaaaadddeeeeerrrfwww'

d = {}
for i in s:
    if i not in d:
        d[i] = 0
    d[i] += 1

print(d)
