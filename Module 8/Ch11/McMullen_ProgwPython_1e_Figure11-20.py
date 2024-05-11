
with open("their_songs.txt", "w") as output_file:
    num_songs = int(input("Hello friend. How many songs would you like to enter? "))
    
    for i in range(num_songs):
        artist = input("Please enter the artist name. ")
        song = input("Please enter the song name. ")
        rating = input("Please enter the rating (1-5).")
        
        output_file.write(artist + "," + song + "," + rating + "\n")
    
    print("Thanks! Your file has been written.")
