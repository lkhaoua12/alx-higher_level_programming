#!/usr/bin/python3
""" post email and get response """

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    e_mail = sys.argv[2]

    r = requests.post(url, {'email': e_mail})
    print(r.text)
