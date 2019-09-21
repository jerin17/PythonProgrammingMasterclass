import pickle

# imelda = ('More Mayhem',
#           'Imelda May',
#           '2011',
#           ((1, 'Pulling the rug'),
#            (2, 'Psycho'),
#            (3, 'Mayhem'),
#            (4, 'Kentish Town Waltz')))
#
# #write
# with open("imelda.pickle", "wb") as pickle_write:
#     pickle.dump(imelda, pickle_write)
#
# #read
# with open("imelda.pickle", "rb") as pickle_read:
#     imelda2 = pickle.load(pickle_read)
# print(imelda2)
# print()
#
# album, artist, year, tracks = imelda2
# print(album)
# print(artist)
# print(year)
# print()
#
# for i in tracks:
#     sno, song = i
#     print("{}. {}".format(sno, song))

imelda = ('More Mayhem',
          'Imelda May',
          '2011',
          ((1, 'Pulling the rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

#write
with open("imelda.pickle", "wb") as pickle_write:
    pickle.dump(imelda, pickle_write)
    pickle.dump(even, pickle_write)
    pickle.dump(odd, pickle_write)
    pickle.dump(29998302, pickle_write)
    pickle.dump(123, pickle_write)

#read
with open("imelda.pickle", "rb") as pickle_read:
    imelda2 = pickle.load(pickle_read)
    even_list = pickle.load(pickle_read)
    odd_list = pickle.load(pickle_read)
    x = pickle.load(pickle_read)
    y = pickle.load(pickle_read)

print(imelda2)
print()

album, artist, year, tracks = imelda2
print(album)
print(artist)
print(year)
print()

for i in tracks:
    sno, song = i
    print("{}. {}".format(sno, song))

print()
for i in odd_list:
    print(i, end='')
print()
for i in even_list:
    print(i, end='')
print()
print(x)
print(y)


# Delete a file using pickle.load
# pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR.")
