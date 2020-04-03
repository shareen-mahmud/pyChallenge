imelda = "More Mayhem", "Imelda May", 2011, ((1, "Pulling the Rug"), (2, "Unknown"), (3, "New"))
name, artist, year, songs = imelda
print(name)
print(artist)
print(year)
for song in songs:
    track, name = song
    print(track, name)
