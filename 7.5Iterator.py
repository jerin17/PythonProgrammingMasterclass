string = "1234567890"

for i in string:
    print(i)

my_iterator = iter(string)
print(my_iterator)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print()
print()
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
iterator = iter(my_list)

for i in range(len(my_list)):
    print(next(iterator))