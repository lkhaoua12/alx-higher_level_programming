#!/usr/bin/python3
""" handle HTTPerror expections """

from urllib import request
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with request.urlopen(url) as reponse:
            print(reponse.read())
    except HTTPError as e:
        print(f'Error code: {e.code}')
