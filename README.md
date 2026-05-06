["# Training_projects" ]

https://roadmap.sh/projects/task-tracker

Task Tracker CLI versaion (2.0)

This is a CLI application built with Python. This project was developed as part of the project found on https://roadmap.sh/projects/task-tracker

**About the Project** 

The core objective of this project was to transition from basic interactive `input()` loops to a professional **CLI-driven approach** using `sys.argv` module. Instead of having the program lead the user and wait for the inputs it can be called directly from the terminal.

**Key Features:**
- **Persistent Storage**: All tasks are saved and managed in a `tasks.json` file.
- **Dynamic ID Management**: Automatically assigns unique identifiers to new tasks.
- **Advanced Filtering**: View all tasks or filter them by status (e.g., `todo`, `in-progress`, `done`).
- **Timestamping**: Automatically tracks creation time (`createdAt`) and the last update time (`updatedAt`).

**Installation & Usage**

1. Ensure you have Python 3.x installed.
2. Clone this repository or download the `tasks.py` file.
3. Run the commands directly from your terminal:

### Command Examples:

**Adding a new task:**
```bash
python tasks.py add "Buy groceries" todo
```


-------------------------------------------------------------------


**Version history:**

This is a project used to practice coding in Python version 1.0 as part of the project found on: https://roadmap.sh/projects/task-tracker

This is the initial, interactive version of the Task Tracker tool built. It is a user-friendly, menu-driven experience using loops and real-time input.

**About this version**

My goal was to create a script that runs an interactive loop where the user is prompted to select actions from a menu. It's designed for a "guided" user experience. I imagine this is how a very simple, robust task tracker could work and be used.

**Key Features:**

Interactive Menu: Users select actions (Add, Update, Delete, List) by typing numbers or keywords.
Guided Inputs: The program asks step-by-step for the task name, ID, or status.
Continuous Session: The program stays open in a while True loop until the user chooses to exit.
JSON Persistence: Saves and loads data from tasks.json so that once the program is closed the inputs are not lost

**How to Run**

Open your terminal.
Run the script:
```bash
python main.py
```
Follow on-screen instructions
