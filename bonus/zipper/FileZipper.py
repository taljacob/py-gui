import FreeSimpleGUI as SG
from zip_compressor import archive_files



label1 = SG.Text("Select files to zip:", size=(15, 1), justification='left')
input_bo1x = SG.Input(key='sources')
choose_button1 = SG.FilesBrowse("Choose")

label2 = SG.Text("Select target folder:", size=(15, 1), justification='left')
input_box2 = SG.Input(key='target')
choose_button2 = SG.FolderBrowse("Choose")

button_zip = SG.Button("Zip")
output = SG.Text( key='output', text_color='#69ff7f', font=('Helvetica', 15))

window = SG.Window("File zipper", layout=[
    [label1, input_bo1x, choose_button1],
    [label2, input_box2, choose_button2],
    [button_zip, output]])

while True:
    event, values = window.read()
    print(f"event: {event}, values: {values}")
    match event:
        case "Zip":
            sources = values['sources'].split(';')
            target_folder = values['target']
            archive_files(sources, target_folder)
            window['output'].update("Archived successfully!")
        case SG.WIN_CLOSED:
            break



window.close()