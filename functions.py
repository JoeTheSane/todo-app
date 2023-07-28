FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Reads data from the file named in the argument
    and returns list of todo items.
    Default is ./todos.txt"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Writes todos list to the file
    named in the argument
    Default is ./todos.txt"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)