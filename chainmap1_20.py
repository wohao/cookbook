from collections import ChainMap

a = {'x':1,'z':2}
b = {'y':2,'z':3}
c = ChainMap(a,b)
print(c['x'])
print(c['y'])
print(c['z'])
print(len(c))
values = ChainMap()
values['x']=1
values = values.new_child()
values['x']=2
print(values)