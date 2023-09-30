#!/usr/bin/python3
""" module doc """
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        data = response.read()
        utf_data = data.decode('utf-8')
        c_type = type(data)

        print("Body response:")
        print(f"\t- type: {c_type}")
        print(f"\t- content: {data}")
        print(f"\t- utf8 content: {utf_data}")
