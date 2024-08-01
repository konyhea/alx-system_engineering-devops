#!/usr/bin/python3
'''import libraries'''
import csv
import requests
import sys


def gather_data_from_API(employee_id):
    '''
    using this REST API, for a given employee ID
    returns information about his/her
    TODO list progress.
    '''
    base_url = 'https://jsonplaceholder.typicode.com/'
    # retrieving data from response
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    USER_NAME = user_data["username"]
    # retrieving progress todo
    todo_response = requests.get(
        f"{base_url}/todos", params={"userId": employee_id}
    )
    todo_data = todo_response.json()
    file_name = f"{employee_id}.csv"
    with open(file_name, mode="w") as USER_ID:
        user_writer = csv.writer(
            USER_ID, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL
        )
        for task in todo_data:
            user_writer.writerow(
                [employee_id, USER_NAME, task["completed"], task["title"]]
            )


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    gather_data_from_API(employee_id)
