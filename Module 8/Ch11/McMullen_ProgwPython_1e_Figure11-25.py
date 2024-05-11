import os

folder = input("Enter a folder name: ")
all_files = os.listdir(folder)
count = 0

for file in all_files:
    if file.endswith(".txt"):
        count += 1

print("There are", count, "files ending in .txt.")