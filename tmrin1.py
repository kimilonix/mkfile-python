import os

file_name = input("Enter the file name: ")
file_path = input("Enter the file path (leave blank for current directory): ")

if file_path == "":
    file_path = os.getcwd()
full_file_path = os.path.join(file_path, file_name)

if os.path.exists(full_file_path):
    print("File already exists!")
else:
    os.system(f"touch {full_file_path}")
    print(f"File '{file_name}' created successfully at '{file_path}'")