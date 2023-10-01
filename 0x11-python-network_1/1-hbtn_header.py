#!/usr/bin/python3
""" fetch url and check header value """

import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    # fetching data
    with urllib.request.urlopen(url) as response:
        data = response.headers['X-Request-Id']
        print(data)
