import os

folder = input("Enter a folder name: ")
count = 0
files = os.listdir(folder)

for filename in files:
    if filename.endswith(".txt"):
        count += 1

print(count)
