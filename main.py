from modules import functions
import FreeSimpleGUI as SG

def persist_window(todolist, wind):
    functions.write_todos(todolist)
    wind['todo'].update('')
    wind['todos'].update(values=todolist)


label = SG.Text("Type in a ToDo", font=('Helvetica', 20), background_color='#05041a', text_color='white')

input_box = SG.InputText(tooltip="Enter a todo item", key="todo")
add_button = SG.Button("Add")

todos = functions.read_todos()
list_box = SG.Listbox(values=todos, key='todos',
                      enable_events=True, size=[45, 10])
edit_button = SG.Button("Edit")
complete_button = SG.Button("Complete")
button_column = SG.Column([[edit_button], [complete_button]], background_color='#05041a')

exit_button = SG.Button("Exit", button_color='red', tooltip="Exit the app")

layout = [
    [label],
    [input_box, add_button],
    [list_box, button_column], [exit_button]
]

window = SG.Window(
    "ToDo App",
    layout=layout,
    font=('Helvetica', 20),
    background_color='#05041a')


while True:
    ## display the window and wait for an event
    event, values = window.read()
    print(f"event: {event}, values: {values}")
    match event:
        case "Add":
            todos.append(values['todo'] + '\n')
            persist_window(todos, window)
        case "Edit":
            edit_todo = values['todos'][0]
            new_todo = values['todo']
            if new_todo:
                todos[todos.index(edit_todo)] = new_todo + '\n'
                persist_window(todos, window)
        case "Complete":
            complete_todo = values['todos'][0]
            todos.remove(complete_todo)
            persist_window(todos, window)
        case SG.WIN_CLOSED | "Exit":
            break

## close the window
window.close()