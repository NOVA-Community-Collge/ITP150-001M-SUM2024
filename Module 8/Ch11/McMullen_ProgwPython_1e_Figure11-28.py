import os

folder = input("Enter a folder name: ")
all_files = os.listdir(folder)
removed_files = 0

for file in all_files:
    file_path = os.path.join(folder, file)
    if os.path.isfile(file_path) and not file.endswith(".txt"):
        os.remove(file_path)
        removed_files += 1

print(removed_files, "files were removed.")