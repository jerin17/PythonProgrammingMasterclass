# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

my_str = "Python is a very powerful language"
vowels = frozenset("aeiou")

new_str = set(my_str).difference(vowels)
print(new_str)

my_list = list(sorted(new_str))
print(my_list)