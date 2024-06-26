#!/usr/bin/python3
"""
A Python script that uses a REST API, for a
given employee ID to return information about
his/her TODO list progress.
This script goes further to record all tasks that
are owned by the employee into a JSON file of the format:
"USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, {"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, ... ]}
The JSON file name is of the format: USER_ID.csv
"""

import json
import requests


if __name__ == "__main__":
    usersUrl = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(usersUrl)
    users = response.json()

    myJSONdict = {}
    for user in users:
        userId = user.get('id')
        username = user.get('username')
        userUrl = 'https://jsonplaceholder.typicode.com/users/{}'.format(
                userId)
        userTodoUrl = str(userUrl + "/todos")
        userTodoDetails = requests.get(userTodoUrl)
        userTodoDetailsJSON = userTodoDetails.json()
        myJSONdict[userId] = []
        for task in userTodoDetailsJSON:
            myJSONdict[userId].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
                })
    # Writing into the JSON file
    with open('todo_all_employees.json', 'w') as myJSONFile:
        json.dump(myJSONdict, myJSONFile)
        # myJSONFile will be todo_all_employees.json
