#!/usr/bin/python3
for int in range(0, 90):
    if (int / 10) == (int % 10):
        continue
    elif (str(int / 10)) in (str(int)) and (str(int % 10)) in (str(int)):
        continue
    elif int != 89:
        print('{:02d},'.format(int), end=' ')
    else:
        print('{}'.format(int))
