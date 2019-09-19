# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for i in farm_animals:
#     print(i)
# print()
#
# wild_animals = set(["lion", "tiger", "panther", "elephant"])
# print(wild_animals)
# for i in wild_animals:
#     print(i)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)

# empty_set1 = set()
# empty_set2 = {}         # this will be taken as dictinary and dict doesnt have add method
# empty_set1.add("a")
# empty_set2.add("a")


# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# square_tuple = {4, 9, 16, 25, 36}
# squares = set(square_tuple)
# print(squares)
# print(len(squares))
# print()
#
# print(even.union(squares))
# print(len(even.union(squares)))
# print()
#
# print(even.intersection(squares))
# print(even & squares)
# print(len(even.intersection(squares)))

even = set(range(0, 40, 2))
print(sorted(even))
square_tuple = {4, 9, 16, 25, 36}
squares = set(square_tuple)
print(sorted(squares))

print("even minus square : ")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("square minus even : ")
print(sorted(squares.difference(even)))
print(sorted(squares - even))

