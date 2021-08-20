#!/usr/bin/python3
''' fetches https://intranet.hbtn.io/status '''
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


url = 'https://intranet.hbtn.io/status'
try:
    with urlopen(url) as result:
        output = result.read()
        print('Body response:')
        print('\t - type: {}'.format(type(output)))
        print('\t - content: {}'.format(output))
        print('\t - utf8 content: {}'.format(output.decode('utf-8')))
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
