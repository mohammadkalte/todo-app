import functions

while True:
    user_acion = input("Enter add, show, edit, complete, or exit : ")
    user_acion = user_acion.strip()
    if user_acion.startswith('add'):
        todo = user_acion[4:] + '\n'
        todos = functions.get_todos()
        todos.append(todo)
        functions.wite_todos(todos)
    elif user_acion.startswith('show'):
        todos = functions.get_todos()
        for index,todo in enumerate(todos):
            todo = todo.strip('\n')
            print(f"{index+1}-{todo}")
    elif user_acion.startswith('edit'):
        number = int(user_acion[5:])
        new_todo = input('Enter new todo : ') +'\n'
        todos = functions.get_todos()
        todos[number - 1] = new_todo
        functions.wite_todos(todos)
    elif user_acion.startswith('complete'):
        number = int(user_acion[8:])
        todos = functions.get_todos()
        todos.pop(number -1)
        functions.wite_todos(todos)
    elif user_acion.startswith('exit'):
        break
    else:
        print("")