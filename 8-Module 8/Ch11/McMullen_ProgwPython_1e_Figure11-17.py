
file_variable = open("songs.txt", "r")

artist_index = 0
song_index = 1
rating_index = 2

contents = file_variable.read()

split_by_line = contents.split("\n")
split_by_comma = [x.split(",") for x in split_by_line if x != ""]

print("First Artist:", split_by_comma[0][artist_index])
print("First Song:", split_by_comma[0][song_index])
print("First Rating:", split_by_comma[0][rating_index])
