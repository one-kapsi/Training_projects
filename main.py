# Basic commands list - to control what to do with the task(s):
commands = { "add": "Task added successfully",
             "update": "Task updated",
             "delete": "Task deleted",
             "list": "List of tasks:"
}

# List of statues:
status = { "todo",
           "in-progress",
           "done"}

# Setting up ID for tasks:
next_id = 0

#"basket for tasks":

tasks_base = {}


import json
import os
if os.path.exists("tasks.json"):
    with open("tasks.json", "r") as file:
        tasks_base = json.load(file)
        if tasks_base:
            tasks_base = {int(task_id): task_values_with_the_id for task_id, task_values_with_the_id in tasks_base.items()}
            next_id = max(tasks_base.keys())
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks_base, file, indent=4)

# Setting upd date of creation & date pof the update
from datetime import datetime

#Setting up the While loop for the actual logic:

while True:
    select_action = input("Select an action (add, update, delete, list) or type \"q\" to exit: ").lower()
    if select_action == "add":
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task_name = input("Task name: ")
        task_status = input("Task status (todo, in-progress, done): ")
        next_id += 1
        new_task = {
            "name": task_name,
            "status": task_status,
            "ID": next_id,
            "createdAt": now,
            "updatedAt": now
        }
        tasks_base[next_id] = new_task
        save_tasks()
        print(f"Task added successfully, ID: {next_id}")
    elif select_action == "update":
        select_task_id = int(input("provide id of the task to update: ")) # I need to have interger as input always returns string
        if select_task_id in tasks_base: #checking if the task id exists
            updated_status = input(" provide new status ( todo, in-progress, done): ") # providing new status
            tasks_base[select_task_id]["status"] = updated_status # Now I need to get into the base of tasks and look for ID from the input
                                                                    # and I am looking at status in the new_task variable
            tasks_base[select_task_id]["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks()
            print(f"Task {select_task_id} updated successfully")
        else:
            (print(f"Task {select_task_id }not found! in the database")) # Here I am doing a failsafe in case ID is not found so user sees error
    elif select_action == "delete":
        select_task_id = int(input("provide id of the task to delete: "))
        if select_task_id in tasks_base:
            confirm_deletion = input(f"Are you sure you want to delete the task with ID {select_task_id}? (y/n): ").lower()
            if confirm_deletion == "y":
                del tasks_base[select_task_id]
                print(f"Task {select_task_id} deleted successfully")
                save_tasks()
            else:
                print(f"Task {select_task_id} was not deleted")
        else:
            print(f"Task {select_task_id }not found!")
            continue
    elif select_action == "list":
        if not tasks_base:
            print("Tasks list is empty!")
        else:
            print(f"Tasks available in database:")
            for task in tasks_base:
                print(f"Task ID: {tasks_base[task]['ID']}")
                print(f"Task name: {tasks_base[task]['name']}")
                print(f"Task status: {tasks_base[task]['status']}")
                print(f"Task createdAt: {tasks_base[task]['createdAt']}")
                print(f"Task updatedAt: {tasks_base[task]['updatedAt']}")
                print("-----")
    elif select_action == "q":
        exit()
    else:
        print("Invalid action, please try again!")
        continue