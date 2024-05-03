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
    todoUrl = employeeUrl + "/todos"
    todoUrl = str(todoUrl)
    todoResponse = requests.get(todoUrl)
    tasks = todoResponse.json()

    myJSONdict = {employeeId: []}
    for task in tasks:
        myJSONdict[employeeId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
            })
    # Writing into the JSON file
    with open('{}.json'.format(employeeId), 'w') as myJSONFile:
        json.dump(myJSONdict, myJSONFile)
        # myJSONFile will be employeeId.json
    """
    # Storing the user data into a UserId.json file
    with open('{}.json'.format(employeeId), 'w') as myJSONFileObject:
        for task in tasks:
            json.dumps(myJSONFileObject.write(
                '{}: {task: {},
                completed: {},
                username: {}},\n'.format(
                employeeId,
                task.get('title'),
                task.get('completed'),
                username,
                task.get('title'))))
            json.dumps(myJSONFileObject)
    # We use a for loop to access the TaskCompletedStatus
    # and the TaskTitle because it increases, as shown
    # on the example on the intranet
    """
