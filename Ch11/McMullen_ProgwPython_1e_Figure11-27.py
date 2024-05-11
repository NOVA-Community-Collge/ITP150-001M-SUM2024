import os

folder = input("Enter a folder name: ")
filename = input("Enter a file name: ")
path = os.path.join(folder, filename)

if os.path.exists(path):
    print("The path", path, "exists.")
else:
    print("The path", path, "does not exist.")