# cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]
#
# with open("citi.txt", 'w') as city_file:
#     for i in cities:
#         print(i, file=city_file,flush=True)

# cities = []
# with open("citi.txt", 'r') as city_file:
#     for i in city_file.readlines():
#         cities.append(i.strip('\n'))
#
# print(cities)
# for i in cities:
#     print(i)

# imelda = "More Meyhem", "Imelda May", "2011", (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# with open("imelda3.txt", "w") as imelda_file:
#     print(imelda, file=imelda_file)
with open("imelda3.txt", 'r') as imelda_file:
    content = imelda_file.readline()

imelda = eval(content)
print(imelda)
title, artist, year, track= imelda
print(title)
print(artist)
print(year)
