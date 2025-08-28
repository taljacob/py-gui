from modules import functions
import FreeSimpleGUI as sg


label = sg.Text("Type in a ToDo")
input_box = sg.InputText(tooltip="Enter a todo item", key="todo")
add_button = sg.Button("Add")

window = sg.Window("ToDo App",
                   layout=[
                       [label],
                       [input_box, add_button]
                    ])



## display the window and wait for an event
window.read()


## close the window
window.close()