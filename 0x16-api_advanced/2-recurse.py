#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given
subreddit. If no results are found for the given subreddit, the
function should return None.
Hint: The Reddit API uses pagination for separating pages of responses.
"""


from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit. If no results are
    found for the given subreddit, the function should return None.
    Arguments:
        subreddit (string): the subreddit to search for
    """
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    # parameters = {'after': after}
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after)
    response = get(
        url,
        headers=headers,
        allow_redirects=False)
    results = response.json()

    if response.status_code == 200:
        for children in results.get('data').get('children'):
            hot_list.append(children.get("data").get("title"))

        after = results.get('data').get('after')
        if not after:
            return hot_list
        return recurse(subreddit, hot_list, after)
    else:
        return None
