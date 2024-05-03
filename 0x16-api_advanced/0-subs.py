#!/usr/bin/python3
"""
A function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""


from requests import get


def number_of_subscribers(subreddit):
    """
    A function that returns the number of subscribers
    for a given subreddit.
    Arguments:
        subreddit (str): The subreddit to query.
    Returns:
        The number of subscribers, or 0 if the subreddit is invalid.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = {"User-Agent": "Mozilla/5.0"}
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get("data").get("subscribers")

    except Exception:
        return 0
