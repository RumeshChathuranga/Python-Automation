from pathlib import Path

root_dir = Path("FilesAndFolders/AddPrifixToAllFiles/files")

file_paths = root_dir.iterdir()


for path in file_paths:
    new_filenames = "new-"+ path.stem + path.suffix
    new_filepath = path.with_name(new_filenames) #create a new path using existing path using with new name
    print(new_filepath)
    path.rename(new_filepath)