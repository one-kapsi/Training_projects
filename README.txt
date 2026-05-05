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