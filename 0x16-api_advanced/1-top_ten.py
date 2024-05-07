#!/usr/bin/python3
"""Function to query Reddit API"""


import requests


def top_ten(subreddit):
    """Returns ls of titles of the first ten hot posts"""
    link = 'https://www.reddit.com/r/{}/hot.json'
    usr = {'User-Agent': 'Linux David'}
    heads = []

    try:
        response = requests.get(link.format(subreddit),
                                headers=usr, params={'limit': 10},
                                allow_redirects=False)

        if response.status_code == 200:
            info = response.json()
            posts = info['data']['children']
            for post in posts:
                t = post['data']['title']
                heads.append(t)
        else:
            return None

    except Exception:
        return None

    return heads
