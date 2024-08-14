#!/usr/bin/python3
"""Contains recurse function"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API to retrieve the titles of all hot articles
    for a given subreddit.

    :param subreddit: The subreddit to query.
    :param hot_list: The list that accumulates the hot article titles.
    :param after: The 'after' parameter for pagination.
    :return: A list of titles of all hot articles, or None if the subreddit is invalid.
    """
    # Define the URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    # Set the parameters for the query, including pagination
    params = {"limit": 100, "after": after}

    # Make the request to the Reddit API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check if the request was successful
    if response.status_code != 200:
        return None

    # Parse the JSON response
    data = response.json()

    # Check if there are any hot articles
    if "data" not in data or "children" not in data["data"]:
        return None

    # Append the titles of the hot articles to the list
    for post in data["data"]["children"]:
        hot_list.append(post["data"]["title"])

    # Check if there is a next page (pagination)
    after = data["data"]["after"]

    # If there is a next page, recursively call the function
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
