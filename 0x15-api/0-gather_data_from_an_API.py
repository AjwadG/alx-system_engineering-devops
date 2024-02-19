#!/usr/bin/python3
"""
    0-gather_data_from_an_API module
    take one arg the id number
    sends a get req to an api
    to get the name o user
    and all its task then print them
"""
import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    usr = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todo = "https://jsonplaceholder.typicode.com/todos?userId={}".format(id)
    usr = requests.get(usr).json()
    todo = requests.get(todo).json()
    done = []
    for task in todo:
        if task.get("completed"):
            done.append(task)
    print("Employee {} is done with tasks({}/{}):".format(usr.get("name"),
                                                          len(done),
                                                          len(todo)))
    for task in done:
        print("\t {}".format(task.get("title")))
