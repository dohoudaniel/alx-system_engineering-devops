#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given
subreddit. If no results are found for the given subreddit, the
function should return None.
Hint: The Reddit API uses pagination for separating pages of responses.
"""


from requests import get
after = None


def recurse(subreddit, hot_list=[]):
    """
    Queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit. If no results are
    found for the given subreddit, the function should return None.
    Arguments:
        subreddit (string): the subreddit to search for
    """
    global after
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    parameters = {'after': after}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = get(url, headers=headers, params=limit, allow_redirects=False)
    results = response.json()

    try:
        afterData = results.get('data').get('after')
        if afterData is not None:
            afterDetails = afterData
            recurse(subreddit, hot_list)
        allData = results.get('data').get('children')
        for postTitle in allData:
            hot_list.append(postTitle.get('data').get('title'))
        return hot_list
    else:
        return None
