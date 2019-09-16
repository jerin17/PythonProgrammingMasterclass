print(range(100), end="\n\n")

my_list = list(range(10))
print(my_list, end='\n')

odd = list(range(1, 50, 2))
even = list(range(2, 51, 2))
print(odd)
print(even)
print()

my_string = "abcdefghijklmnopqrstuvwxyz"
print(my_string.index('e'))
print(my_string[4])

my_number = range(0, 10)
print(my_number)
print(my_number.index(3))

x = range(0, 100000, 2)
print(x)
print(x[976])
print()

sevens = range(7, 1000000, 7)
num = int(input("Please enter a positive number less than a million : "))
if num in sevens:
    print("Well, {} is a multiple of seven.\n".format(num))
else:
    print("Nope, {} is not exactly a multiple of seven.\n".format(num))

my_range = my_number[::2]
print(my_number)
print(my_range)
print(my_number.index(4))
print(my_range.index(4))
print()
r1 = range(0, 100)
print(r1)

r2 = r1[3:40:3]
print(r2)

for i in r2:
    print(i)
print("-" * 40)

for i in r1:
    print(i)
