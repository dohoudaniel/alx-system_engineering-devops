#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit.
"""


from requests import get


def top_ten(subreddit):
    """
    A function that queries the Reddit API and prints the
    4 titles of the first 10 hot posts listed for a given subreddit.
    Arguments:
        subreddit (str): The subreddit to query.
    Returns:
        The number of subscribers, or 0 if the subreddit is invalid.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    limit = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = get(url, headers=headers, params=limit, allow_redirects=False)
    results = response.json()

    try:
        topTenData = results.get('data').get('children')
        for post in topTenData:
            print(post.get('data').get('title'))
    except Exception:
        print("None")
