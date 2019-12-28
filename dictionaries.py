'''a = 'hello world aaasss'
li = list(a)

d ={}

for c in li:
	if d in c:
		d[c] += 1
	else:
		d[c] = 1
'''

import random

#print("Random number between 100 and 999 : ", random.randrange(100,999,5))

print("Generating 3 random integer number between 100 and 999 divisible by 5: ")

for i in range(3):
	print(random.randrange(100,999,5), end=', ')