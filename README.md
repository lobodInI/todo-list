# TODO LIST

## Project Overview

>Manager for monitoring task completion, with the ability to set deadlines and mark completion


## Installation Instructions

To install TODO LIST manager, follow these steps:

- Clone the repository:

    ```bash
    git clone https://github.com/lobodInI/todo-list.git
    ```

- Go to the project directory:

    ```bash
    cd todo_list
    ```

- Install virtual environment and activate it:
   ```bash
    python3 -m venv venv
    source venv/bin/activate
   ```

- Install depending on:

    ```bash
    pip install -r requirements.txt
    ```
 
- Apply migrations:

    ```bash
    python manage.py migrate
    ```
  
- Run server:

    ```bash
    python manage.py runserver
    ```

- Open your browser and check the address (http://127.0.0.1:8000/).

## Usage Guide

1. Add, update, delete tags.
2. Add new tasks, edit existing ones and mark them as completed.


## Configuration

- Creating, editing and deleting tasks.
- Marking tasks as completed.
