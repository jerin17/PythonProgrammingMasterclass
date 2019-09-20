# even = set(range(0, 40, 2))
# square_tuple = {4, 9, 16, 25, 36}
# squares = set(square_tuple)
#
# print(sorted(even))
# print(squares)
# even.difference(squares)
# print("even.difference(squares) : ", sorted(even))
# even.difference_update(squares)
# print("even.difference_update(squares) : ", sorted(even))


# even = set(range(0, 40, 2))
# square_tuple = {4, 9, 16, 25, 36}
# squares = set(square_tuple)
# print(sorted(even))
# print(squares)
# print("even.symmetric_difference(squares) : ", sorted(even.symmetric_difference(squares)))
# print("squares.symmetric_difference(even) : ", sorted(squares.symmetric_difference(even)))


# even = set(range(0, 40, 2))
# square_tuple = {4, 9, 16, 25, 36}
# squares = set(square_tuple)
# print(sorted(even))
# print(squares)
#
# squares.discard(4)
# squares.remove(16)
# squares.discard(8)
# print(squares)
# try:
#     squares.remove(8)
# except KeyError:
#     print("The item 8 is not a member of the set")


# even = set(range(0, 40, 2))
# square_tuple = {4, 6, 16}
# squares = set(square_tuple)
# print(sorted(even))
# print(squares)
#
# if squares.issubset(even):
#     print("square is a subset of even")
# if even.issuperset((squares)):
#     print("even is a super set of squares")

even = frozenset(range(0, 40, 2))
print(sorted(even))
even.add(3)