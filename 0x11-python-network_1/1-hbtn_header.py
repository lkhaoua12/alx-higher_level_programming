#!/usr/bin/python3
""" get request and header file """
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.info()
        request_id = header.get('X-Request-Id')
        if request_id:
            print(request_id)
