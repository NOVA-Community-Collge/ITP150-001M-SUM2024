import os

folder = input("Enter a folder name: ")
all_files = os.listdir(folder)
count = 0

for file in all_files:
    file_path = os.path.join(folder, file)
    if os.path.isdir(file_path):
        count += 1

print("There are", count, "subfolders in", folder + ".")