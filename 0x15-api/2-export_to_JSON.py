#!/usr/bin/python3
"""  Gather data from an API """
import json
import requests
from sys import argv
"""modules to work with"""


def get_employee_todos_progress(employee_id):
    """ a function to return the info about the employee todos progress"""
    try:
        url = "https://jsonplaceholder.typicode.com/"
        user_datas = requests.get(url + f"users/{employee_id}")
        user_data = user_datas.json()
        employee_name = user_data['username']

        """fetch todos list for the employee"""
        todos_list = requests.get(url + f"todos?userId={employee_id}")
        json_todos_list = todos_list.json()

        total_task = len(json_todos_list)
        task_done = [task for task in json_todos_list if task['completed']]
        no_task_done = len(task_done)

        """display the result"""
        print(f"Employee {employee_name} is done with tasks("
              f"{no_task_done}/{total_task}):")

        """title of completed task"""
        for task in task_done:
            print(f"\t {task['title']}")

        """json blocks"""
        tasks = [
                {"task": task["title"],
                 "completed": task["completed"],
                 "username": employee_name
                 }
                for task in json_todos_list
                ]
        new_json_data = {str(employee_id): tasks}

        """exporting data """
        json_filename = f"{employee_id}.json"
        with open(json_filename, mode="w") as json_file:
            json.dump(new_json_data, json_file, indent=4)

    except Exception as e:
        print(f"an error ocuured: {e}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: Script <employee_id>")
    else:
        get_employee_todos_progress(argv[1])
