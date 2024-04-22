#!/usr/bin/python3
"""
Export all data in the JSON format
"""


import json
import requests


if __name__ == "__main__":
    """
    code process:
     - API Base URL
     - Gets all users
     - Initialize dict to store data for all employees
     - Loop through each user
     - Fetch todos for the specified user
     - Loop through todos and makes data for the current user
     - Add user todos data to all employees data
     - Write JSON data to the file
    """
    api_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(api_url + "users").json()
    all_data = {}

    for v in users:
        user_id = v['id']
        user_name = v['username']

        todos = requests.get(api_url + "todos",
                             params={"userId": user_id}).json()
        user_todos = []

        for u in todos:
            user_todos.append({
                "username": user_name,
                "task": u['title'],
                "completed": u['completed']
            })

        all_data[user_id] = user_todos

    json_file = "todo_all_employees.json"

    with open(json_file, 'w') as file:
        json.dump(all_data, file)
