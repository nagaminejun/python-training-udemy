import string

# s = 'test'
with open('template.txt') as f: # section8/template.txt
    t = string.Template(f.read())
print(t)
contents = t.substitute(name='Mike', contents='How are you??')
print(contents)
