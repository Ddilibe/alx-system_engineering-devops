#!/usr/bin/python3
"""
    Script that queries the reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit
"""
import requests

def top_ten(subreddit):
    """ Function that queries the reddit urk to print the first 10
    hot topics  """
    agent = ''
    headers = {
        "User-Agent": agent
    }
    params = {
        "limit":10
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url, headers=headers, params=params,
            allow_redirects=False)
    if request.status_code == 200:
        values = request.json()
        if 'data' in values:
            if 'children' in values['data']:
                post = values['data']['children']
                if len(post):
                    for i in post:
                        print(i['data']['title'])
                    return
    print(None)
    return (0)
