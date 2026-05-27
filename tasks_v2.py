import json
import os
import argparse
import datetime

task_base=[]

if os.path.exists("tasks_v2.json"):
    with open("tasks_v2.json", "r") as file:
        database=json.load(file)
else:
    database=[]

parser = argparse.ArgumentParser(prog = "Task Tracker CLI using argparse", description = "Add, delete, update and list tasks", epilog = "Have fun! :)")

parser.add_argument("-a", "--add", help = "add new task name to database")
parser.add_argument("-s", "--status", help = "add task status")
parser.add_argument("-u", "--update", help = "update existing task", type=int)
parser.add_argument("-d", "--delete", help = "delete task")
parser.add_argument("-l", "--list", help = "show list of all tasks", action = "store_true")
args = parser.parse_args()

if args.list:
        if not database:
            print("Task list is empty")
        else:
            print("-"*50)
            for task in database:
                print(f"ID: {task['ID']:<{4}})| {task ['name']:<{20}}| {task['status']:<{10}}|{task['createdAt']:<{15}}| {task['updatedAt']:<{15}}")
elif args.add:
        name = args.add
        timestamp = datetime.datetime.now().replace(microsecond=0).isoformat()
        status = args.status
        if len(database)==0:
            next_id = 1
        else:
            next_id = database[-1]['ID'] + 1
        new_task = {"ID": next_id,
                        "name": name,
                        "status": status,
                        "createdAt": timestamp,
                        "updatedAt": timestamp}
        database.append(new_task)
        with open("tasks_v2.json", "w") as file:
            json.dump(database, file, indent=4)
            print(f"new task added to database: {name}, status: {status} with ID: {next_id}")
elif args.update:
    id_to_update = int(args.update)
    timestamp = datetime.datetime.now().replace(microsecond=0).isoformat()
    status_to_update = args.status
    task_in_database = False
    for task in database:
        if task['ID'] == id_to_update:
            task['status'] = status_to_update
            task['updatedAt'] = timestamp
            task_in_database = True
    if task_in_database == True:
        with open("tasks_v2.json", "w") as file:
            json.dump(database, file, indent=4)
        print(f"Task {id_to_update} updated to {status_to_update}")
    else:
        print(f"Task {id_to_update} not found in database")
elif args.delete:
    id_to_delete = int(args.delete)
    original_database = len(database)
    database = [task for task in database if task['ID'] != id_to_delete]
    if len(database) < original_database:
        with open("tasks_v2.json", "w") as file:
            json.dump(database, file, indent=4)
        print(f"Task {id_to_delete} removed from database")
    else:
        print(f"Task {id_to_delete} not in database")

