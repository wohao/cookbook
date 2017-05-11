def dedupe(items):
	seen = set()
	for item in items:
		if item not in seen:
			yield item

		seen.add(item)
		print(item)
		print(seen)

a = [1,5,2,1,1,9,1,5,10]

b = list(dedupe(a))
print(b)

def dedupes(items,key=None):
	seen = set()
	for item in items:
		val = item if key is None else key(item)
		if val not in seen :
			yield item
			seen.add(val)

c = [{'x':1,'y':2},{'x':3,'y':2},{'x':1,'y':2},{'x':3,'y':2}]

d = list(dedupes(c,key=lambda d: (d['x'],d['y'])))  #遗留问题输出顺序x，y，  表达式理解
print(d)