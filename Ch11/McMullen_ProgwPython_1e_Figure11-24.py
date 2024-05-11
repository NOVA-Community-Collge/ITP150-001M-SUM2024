import os

folder = input("Enter a folder name: ")
filename = input("Enter a filename: ")

filepath = os.path.join(folder, filename)

print(filepath)