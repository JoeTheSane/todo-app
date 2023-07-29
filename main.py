import functions
import time

user_prompt = "Type a new todo or show, edit, complete, or exit: "
now = time.strftime("%b %d, %Y, %H:%M:%S")
print("It is", now)

while True:
    # Get user input and strip characters
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            todos = functions.get_todos()

            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}. {item}"
                print(row)

            number = int(user_action[5:])
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos()

            number = int(user_action[9:])
            number = number - 1
            todo_to_complete = todos[number].strip('\n')
            todos.pop(number)
            print(f"{todo_to_complete} has been completed.")

            functions.write_todos(todos)

        except IndexError:
            print(f"Item {number +1} does not exist. Please try again.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid")

print("Bye!")
