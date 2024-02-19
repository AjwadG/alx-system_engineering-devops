#!/usr/bin/python3
"""
    3-dictionary_of_list_of_dictionaries module
    sends a get req to an api
    to get all users and tasks
    builds a dict then export as json
"""
from json import dump
import requests


if __name__ == "__main__":
    user = "https://jsonplaceholder.typicode.com/users"
    todo = "https://jsonplaceholder.typicode.com/todos"
    users = requests.get(user).json()
    todos = requests.get(todo).json()
    final = {}
    for task in todos:
        id = str(task.get("userId"))
        new = {"username": users[int(id) - 1].get("username"),
               "task": task.get("title"),
               "completed": task.get("completed")}
        if id in final:
            final.get(id).append(new)
        else:
            final.update({id: [new]})

    with open("todo_all_employees.json", "w+", newline='\n') as f:
        dump(final, f)
