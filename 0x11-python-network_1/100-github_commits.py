#!/usr/bin/python3
""" fetch sha user from github api """


import sys
import requests


def fetch_commit_data(owner, repo_name):
    url = f'https://api.github.com/repos/{repo_name}/{owner}/commits'
    header = {"Accept": "application/vnd.github+json",
              "X-GitHub-Api-Version": "2022-11-28"}
    params = {"per_page": 10}

    response = requests.get(url, headers=header, params=params)
    if response.status_code == 200:
        commit_data = response.json()
        for commit in commit_data:
            commit_sha = commit.get("sha")
            commit_user = commit.get("commit").get("author").get("name")
            result = f'{commit_sha}: {commit_user}'
            print(result)

    else:
        return None


if __name__ == "__main__":
    owner = sys.argv[1]
    repo_name = sys.argv[2]

    fetch_commit_data(owner, repo_name)
