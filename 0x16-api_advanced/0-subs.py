#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    
    :param subreddit: The subreddit to query.
    :return: The number of subscribers, or 0 if the subreddit is invalid.
    """
    # Define the URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    # Make the request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code != 200:
        return 0

    # Parse the JSON response
    data = response.json()

    # Extract the number of subscribers, if available
    if "data" in data and "subscribers" in data["data"]:
        return data["data"]["subscribers"]
    
    return 0
