from functools import partial

record_size = 32

with open('somefile.data','rb') as f:
	records = iter(partial(f.read,record_size),b'')
	for r in records:
		pass