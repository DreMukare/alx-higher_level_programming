#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastDigit = abs(number) % 10
    lastDigit = lastDigit * -1
else:
    lastDigit = number % 10
if lastDigit > 5:
    print('Last digit of {:d} is {:d} and is greater '
    'than 5'.format(number, lastDigit))
elif lastDigit == 0:
    print('Last digit of {:d} is ' 
    '{:d} and is 0'.format(number, lastDigit))
elif lastDigit < 6 and lastDigit != 0:
        print('Last digit of {:d} '
	'is {:d} and is less than 6 '
	'and not 0'.format(number, lastDigit))
