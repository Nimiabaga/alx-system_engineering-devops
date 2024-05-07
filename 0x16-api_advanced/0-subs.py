#!/usr/bin/python3
"""Function to query Reddit API"""


import requests


def number_of_subscribers(subreddit):
    """Gets number of subscribers on a subreddit"""
    link = 'https://www.reddit.com/r/{}/about.json'
    usr = {'User-Agent': 'Linux David'}

    try:
        response = requests.get(link.format(subreddit),
                                headers=usr,
                                allow_redirects=False)
        info = response.json()
        subs = info['data']['subscribers']
        return subs
    except Exception:
        return 0
