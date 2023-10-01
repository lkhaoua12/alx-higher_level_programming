#!/usr/bin/python3
""" fetch data from api with post requests """

import requests
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv[1]) > 1:
        par = sys.argv[1]
    else:
        par = ""

    try:
        req = requests.post(url, data={'q': par})
        res = req.json()
        if res == {}:
            print('No result')
        else:
            print(f"[{res.get('id')}] {res.get('name')}")
    except ValueError:
        print('Not a valid JSON')
