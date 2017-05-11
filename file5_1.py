with open('somefile.txt','wt') as f:
	f.write('I Love You')

f = open('somefile.txt','rt')
data = f.read()

f.close()
with open('D:\python\cookbook\somefile.txt','wt') as f:
	print('Hello world!',file=f)


print('ACME',50,91.5)
print('ACME',50,91.5, sep='')
print('ACME',50,91.5, sep=',')
print('ACME',50,91.5, sep='',end='!!\n')
for i in range(5):
	print(i,end=' ')

rows = ('ACME',50,91.5)
print(','.join(str(x) for x in rows))
print(*rows,sep=',')


with open('somefile.bin','wb') as f:
	f.write(b'Hello world')

with open('somefile.bin','rb') as f:
	data = f.read()
	print(data)
b = b'hello world'
for c in b :
	print(c)


with open('somefile.bin','wb') as f :
	text = 'I love you'
	f.write(text.encode('utf-8'))

with open('somefile.bin','rb') as f:
	data =f.read(16)
	text = data.decode('utf-8')
	print(text)
import array

nums = array.array('i',[1,2,3,4])
with open('data.bin','wb') as f:
	f.write(nums)


a = array.array('i',[0,0,0,0,0,0,0])
with open('data.bin','rb') as f:
	f.readinto(a)
print(a)

# with open('D:\python\cookbook\somefile.txt','xt') as f:
# 	f.write('I love you')

import os
if not os.path.exists('D:\python\cookbook\somefile.txt'):
	with open('D:\python\cookbook\somefile.txt','wt') as f:
		f.write('I love you')

else:
	print('file already exists')


import io
s = io.StringIO()
s.write('hello world\n')
print('this is a test',file=s)
print(s.getvalue())
s =io.StringIO('Hello\nworld\n')
print(s.read(4))
print(s.read())


s = io.BytesIO()
s.write(b'binary data')
print(s.getvalue())

import gzip

with gzip.open('somefile.gz','rt') as f:
	#f.write(text)
	text = f.read()
	print(text)
import bz2 
with bz2.open('somefile.bz2','wt') as f:
	f.write(text)


f = open('somefile.gz','rb')
with gzip.open(f,'rt') as g:
	text = g.read()
