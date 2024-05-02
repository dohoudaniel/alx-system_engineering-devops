#!/usr/bin/python3
"""
A Python script that uses a REST API, for a
given employee ID to return information about
his/her TODO list progress
"""

import requests
from sys import argv as cmdArg


if __name__ == "__main__":
    employeeId = cmdArg[1]
    usersUrl = "https://jsonplaceholder.typicode.com/users"
    employeeUrl = usersUrl + "/" + employeeId

    response = requests.get(employeeUrl)
    employeeName = response.json().get('name')

    todoUrl = employeeUrl + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed') is True:
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
