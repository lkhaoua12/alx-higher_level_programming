#!/usr/bin/python3
""" fetch user id with reqesut module """


import sys
import requests


def fetch_user_id(user, passtoken):
    url = f"https://api.github.com/users/{user}"
    header = {"Authorization": f"basic {user}:{passtoken}"}

    # sending the requests
    response = requests.get(url, headers=header)

    # checking response status
    if response.status_code == 200:
        u_data = response.json()
        u_id = u_data.get('id')
        return u_id
    return None


if __name__ == "__main__":
    user = sys.argv[1]
    passtoken = sys.argv[2]
    result = fetch_user_id(user, passtoken)
    print(result)
