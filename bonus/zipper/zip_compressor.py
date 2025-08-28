import zipfile
import pathlib

def archive_files(source_files, target_folder):
    path = pathlib.Path(target_folder, "archive.zip")
    with zipfile.ZipFile(path, 'w') as archive:
        for filepath in source_files:
            archive.write(filepath, arcname=pathlib.Path(filepath).name)

if __name__ == "__main__":
    archive_files(source_files=["/Users/tyaacov/PycharmProjects/py-gui/files/todos.txt", "/Users/tyaacov/PycharmProjects/py-gui/modules/functions.py"], target_folder="dest")