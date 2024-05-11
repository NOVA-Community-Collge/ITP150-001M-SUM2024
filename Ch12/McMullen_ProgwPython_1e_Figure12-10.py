import os

folder = input("Enter a folder name: ")
count = 0
files = os.listdir(folder)

for filename in files:
    file_path = os.path.join(folder,filename)
    if filename.endswith(".txt"):
        count += 1
    elif os.path.isdir(file_path):
        subfolder_files = os.listdir(file_path)
        for subfilename in subfolder_files:
            if subfilename.endswith(".txt"):
                count += 1

print(count)
