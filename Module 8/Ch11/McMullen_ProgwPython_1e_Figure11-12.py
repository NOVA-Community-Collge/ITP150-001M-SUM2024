try:
    file_variable = open("songs.txt", "r")
except Exception as e:
    print(e)