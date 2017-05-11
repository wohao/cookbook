nums = [1,2,3,4,5,6,7,8,9]
s= sum(x*x for x in nums)
print(s)

import os
files = os.listdir('D:\python\cookbook')
if any(name.endswith('.py') for name in files ):
	print('There be Python')
else:
	print('Sorry ,no python')

s = ('ACME',50,120.23)

print(','.join(str(x) for x in s))

portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]

min_shares = min(s['shares'] for s in portfolio)
print(min_shares)