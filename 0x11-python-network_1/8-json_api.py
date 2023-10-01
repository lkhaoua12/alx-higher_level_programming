#!/usr/bin/python3
""" fetch data from api with post requests """

import requests
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    par = {'q': ""}
    if len(sys.argv) > 1:
        par['q'] = sys.argv[1]

    try:
        res = requests.post(url, data=par)
        r = res.json()
        if r == {}:
            print('No result')
        else:
            print(f"[{r.get('id')}] {r.get('name')}")
    except ValueError:
        print('Not a valid JSON')
