#!/usr/bin/python3
""" fetch header value """

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    try:
        print(r.headers['X-Request-Id'])
    except Exception:
        pass
