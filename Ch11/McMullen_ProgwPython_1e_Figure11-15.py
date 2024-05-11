file_variable = open("songs.txt", "r")
contents = []
two_characters = file_variable.read(2)
while two_characters != "":
    contents.append(two_characters)
    two_characters = file_variable.read(2)
print(contents)