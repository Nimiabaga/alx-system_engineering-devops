#!/usr/bin/python3
"""
Export data in the CSV format
"""


import csv
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
     - Defining CSV filename based on user ID
     - Writing todos data to CSV file
    """
    api_url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(api_url + "users/{}".format(user_id)).json()
    user_name = user.get("username")
    todos = requests.get(api_url + "todos",
                         params={"userId": user_id}).json()

    csv_file = "{}.csv".format(user_id)
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for u in todos:
            writer.writerow([user_id, user_name,
                             u.get("completed"), u.get("title")])
