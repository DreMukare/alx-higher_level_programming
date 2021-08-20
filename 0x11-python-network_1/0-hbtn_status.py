#!/usr/bin/python3
''' fetches https://intranet.hbtn.io/status '''
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


link = 'https://intranet.hbtn.io/status'
req = Request(link)
try:
    with urlopen(req) as result:
        output = result.read()
    print(output)
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
