#!/usr/bin/python3
'''import libraries'''
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
    EMPLOYEE_NAME = user_data.get("name", "unknown")
    # retrieving progress todo
    todo_response = requests.get(
        f"{base_url}/todos", params={"userId": employee_id}
    )
    todo_data = todo_response.json()
    COMPLETED_TASKS = [task for task in todo_data if task.get("completed")]
    TOTAL_NUMBER_OF_TASKS = len(todo_data)
    NUMBER_OF_DONE_TASKS = len(COMPLETED_TASKS)
    print(
        f"Employee {EMPLOYEE_NAME} is done with tasks "
        f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):"
    )
    for task in COMPLETED_TASKS:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    gather_data_from_API(employee_id)
