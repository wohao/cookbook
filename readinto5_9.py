import os.path

def read_into_buffer(filename):
	buf = bytearray(os.path.getsize(filename))
	with open(filename,'rb') as f:
		f.readinto(buf)

	return buf


with open('sample.bin','wb') as f:
	f.write(b"hello world")

buf = read_into_buffer('sample.bin')
print(buf)
print(buf[:5])

with open('newsample.bin','wb') as f:
	f.write(buf)
	print(buf)