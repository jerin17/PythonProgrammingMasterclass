# age = int(input("How old are you ? "))
#
# # if (age >= 16) and (age <=65):
# if 15 < age < 66:
#     print("Have a good day at work")
# else:
#     print("Enjoy . . . ")

# print('''
# False               : {0}
# None                : {1}
# 0                   : {2}
# 0.0                 : {3}
# empty list []       : {4}
# empty tuple ()      : {5}
# empty string ''     : {6}
# empty string ""     : {7}
# empty mapping {{}}    : {8}
# '''.format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool(""), bool({})))

# x = input("Please enter some text ")
# if x:
#     print("\nYou entered '{}'".format(x))
# else:
#     print("\nYou did not enter anything.")
#
# print(True)
# print(False)
# print(not True)
# print(not False)

# age = int(input("How old are you ? "))
# if not (age < 18):
#     print("\nYou're old enough to vote.")
#     print("Please put in your vote in the box.")
# else:
#     print("\nWhoops. Not 18 yet !!!")
#     print("Please come back after {} years please.".format(18-age))

parrot = "Norwegian Blue"
print(parrot)
letter = input("Enter a character : ")

if letter in parrot:
    print("yes. Its in there")
else:
    print("Nope.")