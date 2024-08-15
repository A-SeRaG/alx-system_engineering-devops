#!/usr/bin/python3
'''
    this module contains the function top_ten
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''
        returns the top ten posts for a given subreddit
    '''
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    # Set the parameters for the query to limit to 10 posts
    params = {"limit": 10}

    # Make the request to the Reddit API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check if the request was successful
    if response.status_code != 200:
        print(None)
        return

    # Parse the JSON response
    data = response.json()

    # Check if there are any hot posts
    if "data" not in data or "children" not in data["data"]:
        print(None)
        return

    # Print the titles of the first 10 hot posts
    for post in data["data"]["children"]:
        print(post["data"]["title"])
