tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully")

def view_tasks():
    if not tasks:
        print("No tasks available")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print("Task deleted successfully")
    else:
        print("Invalid task number")

# Sample usage
add_task("Study for SEN 201")
add_task("Complete assignment")
view_tasks()
