#!/usr/bin/python3
'''
takes in url
sends GET request to url
displays body of the response
if error occurs, prints 'Error code:' followed by HTTP status code

Usage: ./7-error_code.py <url>
'''
from sys import argv
import requests

if __name__ == '__main__':
    res = requests.get(argv[1])
    if res.status_code >= 400:
        print('Error code: {}'.format(res.status_code))
    else:
        print(res.text)
