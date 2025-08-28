import FreeSimpleGUI as SG
import zipfile
import os


label1 = SG.Text("Select files to zip:", size=(15, 1), justification='left')
input_bo1x = SG.Input()
choose_button1 = SG.FilesBrowse("Choose")

label2 = SG.Text("Select target folder:", size=(15, 1), justification='left')
input_box2 = SG.Input()
choose_button2 = SG.FolderBrowse("Choose")

button_zip = SG.Button("Zip")

window = SG.Window("File zipper", layout=[
    [label1, input_bo1x, choose_button1],
    [label2, input_box2, choose_button2],
    [button_zip]])

window.read()
window.close()