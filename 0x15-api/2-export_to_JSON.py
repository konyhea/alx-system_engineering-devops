#!/usr/bin/python3
'''Import necessary libraries'''
import json
import requests
import sys


def gather_data_from_API(employee_id):
    '''
    Using this REST API, for a given employee ID,
    returns information about his/her TODO list progress
    and exports it to a JSON file.
    '''
    base_url = 'https://jsonplaceholder.typicode.com'
    # Retrieving user data
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    USER_NAME = user_data["username"]
    # Retrieving TODO list data
    todo_response = requests.get(
        f"{base_url}/todos", params={"userId": employee_id}
    )
    todo_data = todo_response.json()
    # Preparing data for JSON output
    tasks_list = [
        {
            "task": task["title"],
            "completed": task["completed"],
            "username": USER_NAME
        }
        for task in todo_data
    ]
    json_data = {str(employee_id): tasks_list}
    # Writing data to a JSON file
    file_name = f"{employee_id}.json"
    with open(file_name, mode='w') as file:
        json.dump(json_data, file)


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    gather_data_from_API(employee_id)
