from collections import OrderedDict
import json

d = OrderedDict()

d['foo']=1
d['bar']=2
d['spam']=3
d['grok']=4

for key in d :
	print(key,d[key])
json.dumps(d)
print(d)
print(json.dumps(d))