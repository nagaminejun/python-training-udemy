import urllib.request
import json

url = 'http://httpbin.org/get'
with urllib.request.urlopen(url) as f:
    # print(f.read().decode('utf-8'))
    r = print(json.loads(f.read().decode('utf-8')))
    print(type(r))

