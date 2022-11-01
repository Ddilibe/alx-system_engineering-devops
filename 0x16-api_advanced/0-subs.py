#!/usr/bin/python3
"""
    Script that queries the reddit API and returns the number of subscribers
    for a given sub reddit
"""
import requests

def number_of_subscribers(subreddit):
    """ Function that queries the reddit urk for the total numbers of
    subscribers
    """
    agent = ''
    headers = {
        "User-Agent": agent
    }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    request = requests.get(url, headers=headers, allow_redirects=False)
    if request.status_code == 200:
        values = request.json()
        if 'data' in values:
            if 'subscribers' in values['data']:
                return (request.json()['data']['subscribers'])
    return (0)
