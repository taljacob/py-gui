from modules import functions
import FreeSimpleGUI as SG


label = SG.Text("Type in a ToDo")
input_box = SG.InputText(tooltip="Enter a todo item", key="todo")
add_button = SG.Button("Add")

window = SG.Window(
    "ToDo App",
    layout=[[label], [input_box, add_button]],
    font=('Helvetica', 20))

todos = functions.read_todos()
## display the window and wait for an event
while True:
    event, values = window.read()
    print(f"event: {event}, values: {values}")
    match event:
        case "Add":
            todos.append(values['todo'] + '\n')
            functions.write_todos(todos)
        case SG.WIN_CLOSED:
            break

## close the window
window.close()