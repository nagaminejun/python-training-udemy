w = ['Mon', 'Tue', 'Wed']
y = ['coffee', 'tea', 'water']

d = {x: y for x, y in zip(w, y)}
print(d)
