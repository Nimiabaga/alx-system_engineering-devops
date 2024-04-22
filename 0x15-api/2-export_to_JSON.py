#!/usr/bin/python3
"""
Export data in the JSON format
"""


import json
import requests
import sys


if __name__ == "__main__":
    """
    code process:
     - API Base URL
     - Gets user ID
     - Gets user data
     - Extract username from data
     - Fetch todos for the specified user
     - Defining json filename based on user ID
     - Writing JSON data to the file
    """
    api_url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(api_url + "users/{}".format(user_id)).json()
    user_name = user.get("username")
    todos = requests.get(api_url + "todos",
                         params={"userId": user_id}).json()

    json_file = "{}.json".format(user_id)
    with open(json_file, 'w', newline='') as file:
        json_data = {user_id: [
            {
                "task": u.get("title"),
                "completed": u.get("completed"),
                "username": user_name
            }
            for u in todos
            ]}
        json.dump(json_data, file)
