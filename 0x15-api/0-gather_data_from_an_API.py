#!/usr/bin/python3
""" Script that uses the REAT APT to return information about an employees
TODO list progress
"""
if __name__ == '__main__':
    import requests
    import sys
    a, b, new_dict = 0, 0, {}
    name = requests.get('https://jsonplaceholder.typicode.com/users/1/')
    info = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'\
            .format(sys.argv[1]))
    name = name.json().get("name")
    for i in info.json():
        if i.get("completed") == True:
            b += 1
            new_dict[b] = i.get('title')
        a += 1
    print("Employee {} is done with tasks({}/{}):".format(name, b, a))
    for i in new_dict.values():
        print("\t{}".format(i))
