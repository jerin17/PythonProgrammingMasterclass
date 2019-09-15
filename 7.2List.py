parrot = ["non pinin'", "no more,", "a stiff", "bereft of life"]
parrot.append("Norwegian Blue")

for i in parrot:
    print("This parrot is " + i)
print()

odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10]

number = even + odd
print(number)

print(number.sort())
# None

number.sort()
print(number)
print()

list1 = []
list2 = list()

print("List 1 : {}".format(list1))
print("List 1 : {}".format(list1))

if list1 == list2:
    print("Both the lists are equal.")


print(list("Hello world !!!!!"))
print()

even = [2, 4, 6, 8]
another_even = sorted(even, reverse=True)

print(another_even == even)
another_even.sort(reverse=True)
print(even)

numbers = [odd, even]
print(numbers)
print()


for i in numbers:
    print(i)
    for j in i:
        print(j)