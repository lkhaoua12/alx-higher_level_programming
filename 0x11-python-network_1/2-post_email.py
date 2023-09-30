#!/usr/bin/python3
"""sed post request with a parsed email"""


import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    email = sys.argv[2]
    url = sys.argv[1]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        content = response.read().encode('utf-8')
        if content:
            print(content)
