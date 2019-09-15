number = "9, 123, 46, 789, 012, 345"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in "1234567890":
        cleanedNumber += number[i]

print("Number : " + cleanedNumber)

x = 23
x += 1
print(x)

x -= 4
print(x)

x *= 5
print(x)

x /= 4
print(x)

x **= 2
print(x)

x %= 60
print(x)

greetings = "Good"
greetings += "Morning"
print(greetings)

greetings *= 5
print(greetings)