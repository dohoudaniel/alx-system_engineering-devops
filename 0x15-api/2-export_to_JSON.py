#!/usr/bin/python3
"""
Extending 0-gather_data_from_an_API.py to
export data in a JSONN format
"""

import json
import requests
import sys


if __name__ == '__main__':
    employeeID = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeID

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    dictionary = {employeeID: []}
    for task in tasks:
        dictionary[employeeID].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(employeeID), 'w') as filename:
        json.dump(dictionary, filename)
