# tuples are immutable. Can't modify them
t = "a", "b", "c"
print(t)
print("a", "b", "c")
print(("a", "b", "c"))
print()

welcome = "Welcome to my nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the lightening", "Metallica", 1984

print(metallica)
print(metallica[0])
# metallica[0] = "Master of puppets" # wrong
# but
print(imelda)
imelda = imelda[0], "Imelda May", imelda[2]
print(imelda)

metallica2= ["Ride the lightening", "Metallica", 1984]
print(metallica2)
metallica2[0] = "Master of puppets"
print(metallica2)


a = b = c = d = 5
print(c)

a, b = 12, 13
print(a, b)

a, b = b, a
print(a, b)
print()

title, artist, year = welcome
print(welcome)
print(title)
print(artist)
print(year)