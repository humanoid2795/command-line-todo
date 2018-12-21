import json
import os
import sys
from exceptions import TaskDuplicationError


TODO = "todo.json"


class Task(object):

    @staticmethod
    def insert(name, description, limit):
        tasks = None
        try:
            with open(TODO, "r") as todo:
                tasks = json.load(todo)
        except FileNotFoundError:
            raise FileNotFoundError("Initialize the todo file.")
        except json.decoder.JSONDecodeError:
            if os.stat(TODO).st_size == 0:
                tasks = []
            else:
                raise json.decoder.JSONDecodeError("Corrupt todo file.")

        # Checking for unique task name.
        for task in tasks:
            if task["name"] == name:
                raise TaskDuplicationError("A unique task name is required.")

        tasks.append({
            "name": name,
            "description": description,
            "limit": limit
        })

        with open(TODO, "w") as todo:
            json.dump(tasks, todo)

    @staticmethod
    def delete(name):
        tasks = None
        try:
            with open(TODO, "r") as todo:
                tasks = json.load(todo)
        except FileNotFoundError:
            raise FileNotFoundError("The todo file is missing.")
        except json.decoder.JSONDecodeError:
            raise json.decoder.JSONDecodeError("corrupt todo file.")

        updated_tasks = []
        for task in tasks:
            if task["name"] != name:
                updated_tasks.append(task)

        with open(TODO, "w") as todo:
            json.dump(updated_tasks, todo)

    @staticmethod
    def update(name, description, limit):
        tasks = None
        try:
            with open(TODO, "r") as todo:
                tasks = json.load(todo)
        except FileNotFoundError:
            raise FileNotFoundError("Initialize the todo file.")
        except json.decoder.JSONDecodeError:
            if os.stat(TODO).st_size == 0:
                tasks = []
            else:
                raise json.decoder.JSONDecodeError("Corrupt todo file.")

        # Checking for unique task name.
        for task in tasks:
            if task["name"] == name:
                if description is not None:
                    task["description"] = description
                if limit is not None:
                    task["limit"] = limit
                break

        with open(TODO, "w") as todo:
            json.dump(tasks, todo)

    @staticmethod
    def show():
        tasks = None
        try:
            with open(TODO, "r") as todo:
                tasks = json.load(todo)
        except FileNotFoundError:
            raise FileNotFoundError("Initialize the todo file.")
        except json.decoder.JSONDecodeError:
            if os.stat(TODO).st_size == 0:
                sys.stdout.write("Nothing in TODO")
            else:
                raise json.decoder.JSONDecodeError("Corrupt todo file.")

        sys.stdout.write(json.dumps(tasks, indent=4,))
