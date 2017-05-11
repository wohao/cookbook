record = '012345678901234567890123456789'
a = slice(2,4)
b = record[2:4]
c = record[a]
print(b)
print(a)
print(c)

d = slice(5,50,2)
s = 'helloworld'
for i in range(*d.indices(len(s))):
	print(s[i])
