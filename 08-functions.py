# Python Exercise 8. Functions

# a function that receives an arbitrary number of arguments
# def make_salad(*toppings):

# a function that creates an empty dictionary of key/pair values
# def record_user(first_name, last_name, **user_info):

# importing all functions
# from my_code import * 

# importing functions as aliases
# from my_code import my_task as mt

def greet_user(first_name='', last_name='', middle_name=''):
    """Returns a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name, 'middle': middle_name}
    return person


def load_tasks():
    """Prompts user for tasks to complete and returns a list of those tasks."""
    task = 'place_holder'
    task_list = []
    while task != '':
        task = input("Enter a task to complete or leave blank to quit: ")
        if task != '':
            task_list.append(task)
    return task_list


def do_tasks(tasks_to_do):
    """Completes the tasks in the list passed to the function."""
    print("\nNow doing the tasks.")
    task_list = []
    while tasks_to_do:
        current_task = tasks_to_do.pop()
        print("Doing task " + current_task)
        task_list.append(current_task)
    return task_list


def report_tasks(task_list):
    """Prints a list of tasks that have been completed."""
    print("\nThese tasks have been completed:")
    for current_task in task_list:
        print(current_task)


f_name = input("Your first name? ")
l_name = input("Your last name? ")
m_name = input("Your middle name? ")

full_name = greet_user(f_name, l_name, m_name)
print(full_name)
print("\n")

undone_tasks = []
completed_tasks = []
do_more_tasks = 'y'
while do_more_tasks.lower() == 'y':
    undone_tasks = load_tasks()
    completed_tasks = do_tasks(undone_tasks[:])
    report_tasks(completed_tasks)
    do_more_tasks = input("\nStill have more tasks?  Enter 'y' if so or anything else to quit: ")
