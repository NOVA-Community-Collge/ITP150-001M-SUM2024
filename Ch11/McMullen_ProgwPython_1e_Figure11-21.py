with open("songs.txt", "r") as input_file, open("favorite_songs.txt", "w") as output_file:
        
    artist_index = 0
    song_index = 1
    rating_index = 2
    
    contents = input_file.read()
    split_by_line = contents.split("\n")
    split_by_comma = [x.split(",") for x in split_by_line if x != ""]
    final_table = [[line[artist_index], line[song_index], int(line[rating_index])] for line in split_by_comma]
    
    for record in final_table:
        if record[rating_index] >= 4:
            output_file.write(record[artist_index] + "," + record[song_index] + "," + str(record[rating_index]) + "\n")
