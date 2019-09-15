for i in range(1, 21):
    print("i is now : {}".format(i))
print()

number = "9, 123, 456, 789, 012, 345"
for i in range(0, len(number)):
    print(number[i])
print()

for i in range(0, len(number)):
    if number[i] in "1234567890":
        print(number[i], end='')
print()

cleanedNumber = ''
for i in range(0, len(number)):
    if number[i] in "1234567890":
        cleanedNumber = cleanedNumber + number[i]

print("New number : {}".format(cleanedNumber))