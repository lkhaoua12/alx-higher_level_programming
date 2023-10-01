#!/usr/bin/python3
""" fetch data with key=value """

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    argp = sys.argv[2]

    try:
        req = requests.post(url, data={"q": argp})
        req_json = req.json()
        if req_json == {}:
            print('No result')
        else:
            print(f'[{req_json.get("id")}] {req_json.get("name")}')
    except ValueError:
        print('No result')
