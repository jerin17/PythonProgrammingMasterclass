# welcome = "Welcome to my nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Imelda May", 2011, (
#     (1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
# )
#
# print(imelda)
# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)
# print(tracks)
# a, b = tracks[0]
# print(a, b)


# Given the tuple below that represents the Imelda May album "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album.
#
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, separating them with a comma).

# imelda = "More Mayhem", "Imelda May", 2011, (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# print(imelda)

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

title, artist, year, tracks = imelda
print("Title  : " + title)
print("Artist : " + artist)
print("Year   : " + str(year))
print("\nTracks : ")
for i in range(0, len(tracks)):
    sno, song = tracks[i]
    print("{}. {}".format(sno,song))