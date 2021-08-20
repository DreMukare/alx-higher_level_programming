#!/usr/bin/python3
'''
takes in username and personal auth token
use it to access user id through github user API

usage: ./10-my_github.py <username> <auth_token>
'''
from sys import argv
import requests
# from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    username = argv[1]
    pwd = argv[2]
    res = requests.get('https://api.github.com/user', auth=(username, auth))
#    res = requests.request('GET', 'https://apit.github.com/user', (username, pwd))
    print(res.json().get('id'))
