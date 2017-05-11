from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['b'].append(2)
d['b'].append(3)
d['a'].append(2)
d['a'].append(3)
d['b'].append(4)

d['b'].append(4)
f = defaultdict(set)
f['a'].add(1)
f['a'].add(2)
f['b'].add(3)
f['a'].add(2)
f['b'].add(3)

print(d)
print(f)

c = defaultdict(list)
for key ,value in pairs:
	d[key].append(value)

a = {}
for key ,value in pairs:
	if key not in a:
		a[key] = []
	d[key].append(value)