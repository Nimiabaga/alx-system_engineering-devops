#!/usr/bin/python3
"""
Returns information about his/her todo list progress
"""


import requests
import sys


if __name__ == "__main__":
    """
    code process:
     - API Base URL
     - Gets user data
     - Gets todos for the specified user
     - Extract completed tasks
     - Print info about the employee's todo list progress
     - Print titles of tasks completed
    """
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(api_url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(api_url + "todos",
                         params={"userId": sys.argv[1]}).json()
    done = [u.get("title") for u in todos if u.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    [print("\t {}".format(v)) for v in done]
