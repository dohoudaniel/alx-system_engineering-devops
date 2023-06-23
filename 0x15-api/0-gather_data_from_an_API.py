#!/usr/bin/python3

"""
A Python script that uses a REST API, for a given
employee ID, and returns information about his/her
TODO list progress.
"""

# Importing requests for HTTP request
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employee_id

    response = requests.get(url)
    empName = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(empName, done, len(tasks)))

    for employee_task in done_tasks:
        print("\t {}".format(employee_task.get('title')))
