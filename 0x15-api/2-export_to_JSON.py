#!/usr/bin/python3
"""
    2-export_to_JSON.py module
    take one arg the id number
    sends a get req to an api
    to get the name o user
    and all its task then export as json
"""
from json import dump
import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    usr = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todo = "https://jsonplaceholder.typicode.com/todos?userId={}".format(id)
    usr = requests.get(usr).json().get("username")
    todo = requests.get(todo).json()
    final = {id: []}
    for task in todo:
        final.get(id).append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": usr
                })
    with open("{}.json".format(id), "w+", newline='\n') as f:
        dump(final, f)
