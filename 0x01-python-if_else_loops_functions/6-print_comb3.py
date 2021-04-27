#!/usr/bin/python3
num = 0
for i in range(10):
	for n in range(num, 10):
		if i == n:
			continue
		if i == 8 and n == 9:
			print('{:d}{:d}'.format(i, n))
		else:
			print('{:d}{:d}'.format(i, n), end=', ')
		num = num + 1
