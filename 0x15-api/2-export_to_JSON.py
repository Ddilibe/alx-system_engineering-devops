#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import json
import requests
import sys


if __name__ == "__main__":
    address = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1]
    user = '{}users/{}'.format(address, user_id)
    res = requests.get(user)
    json_o = res.json()
    name = json_o.get('username')

    todos = '{}todos?userId={}'.format(address, user_id)
    res = requests.get(todos)
    tasks = res.json()
    l_task = []
    for task in tasks:
        dict_task = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": name}
        l_task.append(dict_task)

    d_task = {str(user_id): l_task}
    filename = '{}.json'.format(user_id)
    with open(filename, mode='w') as f:
        json.dump(d_task, f)
