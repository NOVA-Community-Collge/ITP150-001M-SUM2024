file_variable = open("songs.txt", "r")
contents = []
line = file_variable.readline()
while line != "":
    contents.append(line)
    line = file_variable.readline()
print(contents)