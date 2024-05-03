#!/usr/bin/python3
"""
A Python script that uses a REST API, for a
given employee ID to return information about
his/her TODO list progress.
This script goes further to record all tasks that
are owned by the employee into a CSV file of the format:
UserId, Username, TaskCompletedStatus, TaskTitle
The CSV file name is of the format: UserId.csv
"""

import requests
from sys import argv as cmdArg


if __name__ == "__main__":
    employeeId = cmdArg[1]
    usersUrl = "https://jsonplaceholder.typicode.com/users"
    employeeUrl = usersUrl + "/" + employeeId

    response = requests.get(employeeUrl)
    finalResponse = response.json()
    username = finalResponse.get('username')
    # taskStatus = finalResponse.get('completed')
    # taskTitle = finalResponse.get('title')
    todoUrl = usersUrl + "/todos"
    todoUrl = str(todoUrl)
    todoResponse = requests.get(todoUrl)
    tasks = todoResponse.json()

    # Storing the user data into a UserId.csv file
    with open('{}.csv'.format(employeeId), 'w') as myCSVFileObject:
        for task in tasks:
            myCSVFileObject.write('"{}","{}","{}","{}"\n'.format(
                employeeId,
                username,
                task.get('completed'),
                task.get('title')))
    # We use a for loop to access the TaskCompletedStatus
    # and the TaskTitle because it increases, as shown
    # on the example on the intranet
