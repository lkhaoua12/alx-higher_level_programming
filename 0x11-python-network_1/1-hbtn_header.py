#!/usr/bin/python3
""" fetch url and check header value """

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # fetching data
    with urllib.request.urlopen(url) as response:
        data = response.headers['X-Request-Id']
        print(data)
