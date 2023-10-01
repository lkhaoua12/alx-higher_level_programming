#!/usr/bin/python3
""" fetch data from api with post request """

import requests
import sys

if __name__ == "__main__":
    # Define the URL
    url = "http://0.0.0.0:5000/search_user"

    # Set the default value for the 'q'.
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    # Send the POST request with the 'q' parameter
    response = requests.post(url, data={'q': letter})

    try:
        # Try to parse the response JSON
        result = response.json()

        if result:
            # If JSON is valid and not empty, display id and name
            print("[{}] {}".format(result.get('id'), result.get('name')))
        else:
            # If JSON is empty, display 'No result'
            print("No result")
    except ValueError:
        # If JSON is invalid, display 'Not a valid JSON'
        print("Not a valid JSON")
