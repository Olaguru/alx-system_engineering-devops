#!/usr/bin/python3
"""  Gather data from an API """
import json
import requests
"""modules to work with"""


def get_employee_tasks():
    """ a function to return all info about the employee """
    try:
        url = "https://jsonplaceholder.typicode.com/"
        user_response = requests.get(url + "users")
        user_data = user_response.json()

        """now hold the employee data in dictionary"""
        all_employee_task = {}

        for user in user_data:
            employee_id = user['id']
            employee_name = user['username']

            """ get the todo_list"""
            todo_response = requests.get(url + f"todos?userId={employee_id}")
            todo_list = todo_response.json()

            """prepare the json data"""
            tasks = [
                    {"username": employee_name,
                     "task": task["title"],
                     "completed": task["completed"]
                     }
                    for task in todo_list
                    ]
            all_employee_task[str(employee_id)] = tasks

        json_filename = "todo_all_employees.json"
        with open(json_filename, mode="w") as json_file:
            json.dump(all_employee_task, json_file, indent=4)

    except Exception as e:
        print(f"an error ocuured {e}")


if __name__ == "__main__":
    get_employee_tasks()
