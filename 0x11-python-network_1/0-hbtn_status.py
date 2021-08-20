#!/usr/bin/python3
''' fetches https://intranet.hbtn.io/status '''
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


url = 'https://intranet.hbtn.io/status'
req = Request(url)
try:
    with urlopen(req) as result:
        output = result.read()
        print('Body response:')
        print('\t - type: {}'.format(type(result.read())))
        print('\t - content: {}'.format(output))
        print(
            '\t - utf* content: {}'.format(
                'OK' if "utf-8" in str(result.info()) else 'No'))
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
