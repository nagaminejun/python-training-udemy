import os
import pathlib
import subprocess
import datetime

# print(os.path.exists('template.txt'))
# print(os.path.isfile('template.txt'))
# print(os.path.isdir('test'))
# os.rename('test.txt', 'aaa.txt')
# os.rename('aaa.txt', 'test.txt')
# os.symlink('test.txt', 'testsym.txt')

# pathlib.Path('mkpathlib.txt').touch()

# subprocess.run(['la', '-al'])
now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%d/%m/%y'))

today = datetime.datetime.today()
print(today)
t = datetime.timedelta(days=365)
print(now - t)
