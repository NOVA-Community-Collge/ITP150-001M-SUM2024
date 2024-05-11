

with open("songs.txt", "r") as file_variable:
    contents = file_variable.read()
    
    artist_index = 0
    song_index = 1
    rating_index = 2
    
    split_by_line = contents.split("\n")
    split_by_comma = [x.split(",") for x in split_by_line if x != ""]
    final_table = [[line[artist_index], line[song_index], int(line[rating_index])] for line in split_by_comma]
    song_count = len(final_table)
    
    print("There are", song_count, "songs in the file.")
