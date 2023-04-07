def get_todos():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos


def wite_todos(todos):
    with open('todos.txt', 'w') as file:
        file.writelines(todos)
