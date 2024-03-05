#!/usr/bin/python3
"""
    2-recurse module
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """
        returns list of hot articles of a subreddit recursivly
    """
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    headers = {"User-Agent": "ubuntu:Python (by/AjwadG)"}

    data = requests.get(url, headers=headers, allow_redirects=False)

    if data.status_code != 200:
        return None
    value = data.json().get("data")
    for post in value.get("children"):
        hot_list.append(post.get("data").get("title"))
    after = value.get("after")
    if after:
        recurse(subreddit, hot_list, after)
    return hot_list
