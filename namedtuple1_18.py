from collections import namedtuple
Subscriber = namedtuple('Subscriber',['addr','joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')

print(sub)

print(sub.addr)
print(sub.joined)

print(len(sub))

addr,joined = sub
print(addr)
print(joined)

coms = (['apple',50.0,20.0],['banana',20.0,51.0])

Stock = namedtuple('Stock',['name','shares','price'])
def compute_cost(records):
	total = 0.0
	for rec in records:
		s = Stock(*rec)
		total += s.shares * s.price
	return total

result = compute_cost(coms)
print(result)
