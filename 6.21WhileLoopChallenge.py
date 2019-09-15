import random

highest = 10
answer = random.randint(1, highest)
print(answer)

guess = int(input("Please guess a number between 1 and {} : ".format(highest)))

while guess != answer:
    if guess > answer:
        guess = int(input("Please enter a lower number : "))

    elif guess < answer:
        guess = int(input("Please enter a higher number : "))

else:
    print("\nWaah, mere sher. Ek damm sahi pakde hain !!!")