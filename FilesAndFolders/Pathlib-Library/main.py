from pathlib import Path

p1 = Path('/home/rumeshchathuranga/Documents/GitHub/Python-Automation/FilesAndFolders/Pathlib-Library/files/abc.txt')
print(p1)

if p1.exists():
    with open(p1, 'r') as file:
        print(file.read())

print(p1.name)          # File name with extension
print(p1.stem)          # File name without extension
print(p1.suffix)        # File extension
print(p1.parent)        # Parent directory

p2 = Path('/home/rumeshchathuranga/Documents/GitHub/Python-Automation/FilesAndFolders/Pathlib-Library/files')
for item in p2.iterdir():
    print(item)