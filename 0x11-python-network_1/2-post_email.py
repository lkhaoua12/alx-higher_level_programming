#!/usr/bin/python3
""" fetch url and check header value """

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    e_mail = sys.argv[2]

    # parsing the data
    data = urllib.parse.urlencode({'email': e_mail}).encode('utf-8')

    # posting the data
    with urllib.request.urlopen(url, data) as response:
        data = response.read()
        print(data.decode('utf-8'))
