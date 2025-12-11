from pathlib import Path

root_dir = Path('FilesAndFolders/RenameAllFIles-BasedOnFolder/files')
file_paths = root_dir.glob('**/*') # Recursively get all files and folders instead of iterdir use glob with pattern '**/*'

for path in file_paths:
    if(path.is_file()):
        parent_folder = path.parts[-2]
        new_filename = parent_folder+ '_' + path.name
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)