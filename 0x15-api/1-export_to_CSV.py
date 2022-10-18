#!/usr/bin/python3
""" Script that uses the REAT APT to return information about an employees
TODO list progress
"""
if __name__ == '__main__':
    import csv
    import requests
    import sys
    stringa = 'https://jsonplaceholder.typicode.com/users/{}'
    stringb = 'https://jsonplaceholder.typicode.com/users/{}/todos'
    TOTAL_NUMBER_OF_TASKS, NUMBER_OF_DONE_TASKS = 0, 0
    name = requests.get(stringa.format(sys.argv[1]))
    info = requests.get(stringb.format(sys.argv[1]))
    with open('USER_ID.csv', 'w') as w:
        writer = csv.writer(w)
        EMPLOYEE_NAME = name.json().get("username")
        id = name.json().get('id')
        for i in info.json():
            NUMBER_OF_DONE_TASKS += 1
            TOTAL_NUMBER_OF_TASKS += 1
            writer.writerow(
                    [
                        id,
                        EMPLOYEE_NAME,
                        i.get('completed'),
                        i.get('title')
                        ]
                    )
