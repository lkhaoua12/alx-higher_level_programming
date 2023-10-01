#!/usr/bin/python3
""" fetch data from api with post request """

import requests
import sys

if __name__ == "__main__":
    # Define the URL
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    response = requests.post(url, data={'q': letter})

    try:
        result = response.json()

        if result:
            print("[{}] {}".format(result.get('id'), result.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
