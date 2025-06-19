# ✅ CLI-based To-Do List (Python + Pandas)

A simple **Command Line Interface (CLI)** To-Do List built in Python using basic file handling and the pandas library. This project lets users manage tasks by adding new ones, marking them as done, or resetting the task list.

---

## 📦 Features

- 📋 Add multiple new tasks
- ✔️ Mark tasks as done
- 🔁 Reset the entire list
- 💾 Tasks are stored persistently across sessions using `todo.txt` and `done.txt`
- 📊 Uses `pandas` to display tasks in a clean table

---

## 🧰 Requirements

- Python 3.x
- pandas (`pip install pandas`)
- Jupyter Notebook (`pip install notebook`)

---

## 🚀 Usage

1. Clone the repo:
   ```bash
   git clone https://github.com/Sachin0P/CLi-based-to-do-list.git
   cd CLi-based-to-do-list

  Start Jupyter Notebook:

    jupyter notebook

In the browser window that opens, click on cli_to_do.ipynb to launch the notebook interface. Run the cells one by one using Shift+Enter.

When prompted with:

What would you like to do today?
1. Enter a new task
2. Tick a task
3. Reset the list

Enter:

    1 to add new tasks (you will be asked how many and then for the names)

    2 to tick a task (the list will be shown with indexes; enter the index to mark it done)

    3 to reset both task and done lists (this clears todo.txt and done.txt)
