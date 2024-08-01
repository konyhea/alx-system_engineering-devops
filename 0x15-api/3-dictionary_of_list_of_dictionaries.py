#!/usr/bin/python3
'''Import necessary libraries'''
import json
import requests
import sys


def gather_data_for_all_employees():
    '''
    Using this REST API, retrieves TODO list progress
    for all employees and exports it to a JSON file.
    '''
    base_url = 'https://jsonplaceholder.typicode.com'
    # Retrieving all users
    users_response = requests.get(f"{base_url}/users")
    users_data = users_response.json()
    # Dictionary to store the tasks for all employees
    all_tasks = {}
    for user in users_data:
        user_id = str(user["id"])
        USER_NAME = user["username"]
        # Retrieving TODO list data for each user
        todo_response = requests.get(
            f"{base_url}/todos", params={"userId": user_id}
        )
        todo_data = todo_response.json()
        # Preparing data for each user
        tasks_list = [
            {
                "username": USER_NAME,
                "task": task["title"],
                "completed": task["completed"]
            }
            for task in todo_data
        ]
        # Adding user's tasks to the all_tasks dictionary
        all_tasks[user_id] = tasks_list
    # Writing data to a JSON file
    file_name = "todo_all_employees.json"
    with open(file_name, mode='w') as file:
        json.dump(all_tasks, file)


if __name__ == "__main__":
    gather_data_for_all_employees()
