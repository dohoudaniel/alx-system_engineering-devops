#!/usr/bin/python3
"""
Extending 0-gather_data_from_an_API.py to
export data in the CSV format
"""

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

    with open('{}.csv'.format(employeeID), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employeeID, username, task.get('completed'),
                               task.get('title')))
