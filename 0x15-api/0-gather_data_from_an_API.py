#!/usr/bin/python3
""" Script that uses the REAT APT to return information about an employees
TODO list progress
"""
if __name__ == '__main__':
    import requests
    import sys
    TOTAL_NUMBER_OF_TASKS, NUMBER_OF_DONE_TASKS, new_dict = 0, 0, {}
    name = requests.get('https://jsonplaceholder.typicode.com/user\
                        s/{}'.format(sys.argv[1]))
    info = requests.get('https://jsonplaceholder.typicode.com/users/{}\
                        /todos'.format(sys.argv[1]))
    EMPLOYEE_NAME = name.json().get("name")
    for i in info.json():
        if i.get("completed"):
            NUMBER_OF_DONE_TASKS += 1
            new_dict[NUMBER_OF_DONE_TASKS] = i.get('title')
        TOTAL_NUMBER_OF_TASKS += 1
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for i in new_dict.values():
        print("\t {}".format(i))
